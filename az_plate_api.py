import jetson.inference
import jetson.utils

import argparse
import sys
import cv2

import requests
from pprint import pprint

import threading
import keyboard

# init para
para_PLATE = ['az_plate_api.py', '--model=./networks/az_plate/az_plate_ssdmobilenetv1.onnx', '--class_labels=./networks/az_plate/labels.txt', 
'--input_blob=input_0', '--output_cvg=scores', '--output_bbox=boxes', '--camera=/dev/video0', '--width=640', '--height=480']


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="none", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--overlay_ocr", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0) 

# Func
def crop_img (img, crop_roi, size):
    crop_img = jetson.utils.cudaAllocMapped(width=size[0], height=size[1], format=img.format)
    jetson.utils.cudaCrop(img, crop_img, crop_roi)
    return crop_img

def resize_img (img, size):
    resize_img = jetson.utils.cudaAllocMapped(width=size[0], height=size[1], format=img.format)
    jetson.utils.cudaResize(img, resize_img)
    return resize_img

def ocr_api (img_path):
    regions = ['vn'] # Change to your country
    try:
        with open(img_path, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),  # Optional
                files=dict(upload=fp),
                headers={'Authorization':'Token NUMBER OF YOUR TOKEN'})
        char = response.json()['results'][0]['plate']
        print('[RESULT]: ', char)
    except:
        print('[INFOR]: Processing')

# SIZE plate for OCR
SIZE_FOR_OCR = (340, 180)
plate_path = "plate.jpg"

# load the object detection network
net_PLATE = jetson.inference.detectNet(opt.network, para_PLATE, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=para_PLATE)
# output = jetson.utils.videoOutput(opt.output_URI, argv=para_PLATE+is_headless)
output = jetson.utils.videoOutput(opt.output_URI, argv=para_PLATE+is_headless)
# output = jetson.utils.videoOutput("display://0")

# process frames until the user exits
while True:
    # capture the next image
    img = input.Capture()

    # detect objects in the image (with overlay)
    detections = net_PLATE.Detect(img, overlay=opt.overlay)
    # for detection in detections:
        # print(detection)

    # render the image
    output.Render(img)

    # update the title bar
    # output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net_PLATE.GetNetworkFPS()))
    # print("[INFOR]: FPS is ", net_PLATE.GetNetworkFPS())
    # print out performance info
    # net_PLATE.PrintProfilerTimes()

    if not input.IsStreaming() or not output.IsStreaming():
        break

    if keyboard.is_pressed('c'):
        print('[INFOR]: Looking for plate')
        try:
            if len(detections) != 0:
                ROI_PLATE = (int(detections[0].Left), int(detections[0].Top), int(detections[0].Right), int(detections[0].Bottom))
                SIZE = ((ROI_PLATE[2]-ROI_PLATE[0]), (ROI_PLATE[3]-ROI_PLATE[1]))
                img_crop_plate = crop_img(img, ROI_PLATE, SIZE)
                resize_img_for_ocr = resize_img(img_crop_plate, SIZE_FOR_OCR)
                jetson.utils.saveImage(plate_path, resize_img_for_ocr)
                
                ocr_thread = threading.Thread(target=ocr_api, args=(plate_path,), daemon=False)
                ocr_thread.start()
        except:
            print('[WARNNING]: Focus camera on plate')




