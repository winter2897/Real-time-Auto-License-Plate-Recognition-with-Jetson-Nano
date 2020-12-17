<img src="./images/githubtitle.png" width="100%">

# License Plate Recognition

## Introduction

License PLate Recognition is a source code that detects license plates in pictures or videos. This project was developed to work in real time on **`Jetson Nano`** with **`39 FPS`**. It can detect all kinds of number plates of vehicles in Vietnam.

<div align='center'>
  <img src="./images/ocr_result.gif" width="60%">
</div>

License PLate Detection is a guide for training a custom model for your own license plate dataset and more.

## Run

First, you need to download the full source code and the files are contained in the directory with the following structure:

    License PLate Detection/
      networks/
          -az_plate/
              -az_ocr_ssdmobilenetv1_2.onnx
              -labels.txt
      detectnet-camera.py
      requirements.txt    

You can download the trained model [here](https://drive.google.com/file/d/1wTTWONFUXRBtSKA-Cq3snL21KXCB80PS/view?usp=sharing "model ocr").

<details>
<summary>Recompiled the model with Jetson Nano.</summary>
<br/>

> Note: You should see the file `az_ocr_ssdmobilenetv1_2.onnx.1.1.7103.GPU.FP16.engine`, this file is the model compiled from `az_ocr_ssdmobilenetv1_2.onnx` and ready to run the demo. If you want to try recompiling the file `az_ocr_ssdmobilenetv1_2.onnx`, just delete the file `az_ocr_ssdmobilenetv1_2.onnx.1.1.7103.GPU.FP16.engine`.

</details>

Below are the commands for running a demo with this project. Use the command that matches the type of camera you are using with the Jetson Nano:

**1. MIPI CSI cameras:**

MIPI CSI cameras are compact sensors that are acquired directly by the Jetson's hardware CSI/ISP interface. Supported CSI cameras include:
* [Raspberry Pi Camera Module v2](https://www.raspberrypi.org/products/camera-module-v2/ "Pi Camera") (IMX219) for Jetson Nano and Jetson Xavier NX
* OV5693 camera module from the Jetson TX1/TX2 devkits.  
* See the [Jetson Partner Supported Cameras](https://developer.nvidia.com/embedded/jetson-partner-supported-cameras "Jetson Cam") page for more sensors supported by the ecosystem.

```python
python3 detectnet-camera.py --model=./networks/az_ocr/az_ocr_ssdmobilenetv1_2.onnx --class_labels=./networks/az_ocr/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes --camera=csi://0 --width=640  --height=480
```

**2. V4L2 cameras:**

USB webcams are most commonly supported as V4L2 devices, for example Logitech [C270](https://www.logitech.com/en-us/product/hd-webcam-c270 "C270") or [C920](https://www.logitech.com/en-us/product/hd-pro-webcam-c920 "C920").


```python
python3 detectnet-camera.py --model=./networks/az_ocr/az_ocr_ssdmobilenetv1_2.onnx --class_labels=./networks/az_ocr/labels.txt --input_blob=input_0 --output_cvg=scores --output_bbox=boxes --camera=/dev/video0 --width=640  --height=480
```

**3. RTSP:**

RTSP network streams are subscribed to from a remote host over UDP/IP.

```python
python3 detectnet-camera.py --model=./networks/az_ocr/az_ocr_ssdmobilenetv1_2.onnx --class_labels=./networks/az_ocr/labels.txt --input_blob=input_0 --input-codec=h264 --output_cvg=scores --output_bbox=boxes --camera=rtsp://username:password@<remote-ip>:1234 --width=640  --height=480
```

> Note: Advanced Video Coding RTSP: `H264`

## Training

You can retrain your License PLate Recognition model with a larger set of data by following the tutorial with [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1orv9J1zn_LxSHGG3fwtrAJvCzvugYYbg/view?usp=sharing "Real-time Vietnamese Auto License Plate Recognition with Jetson Nano"). 
> **Download:** You can download the [ssd.zip](https://drive.google.com/file/d/1G9ec7kd2lNspMXlKqvOTE4efjlmfV8Sp/view?usp=sharing) file here.