<img src="./doc/images/githubtitle.png" width="100%">

# Real-time Auto License Plate Recognition with Jetson Nano

**Visit my project on Nvidia Page:** [Jetson Community Projects](https://developer.nvidia.com/embedded/community/jetson-projects#real_time-alpr_jetson_nano)

This repository provides you with a detailed guide on how to build a real-time license plate detection and recognition system. The source code of the repository implemented on Jetson Nano reached 40 FPS.

<div align='center'>
  <img src="./doc/images/ocr_result.gif" width="60%">
</div>

The license plate data set for this repository was collected in Vietnam. You can train your model to detect and recognize number plates by following the instructions below.

### Table of Contents

- [Real-time Auto License Plate Recognition with Jetson Nano](#real-time-auto-license-plate-recognition-with-jetson-nano)
    - [Table of Contents](#table-of-contents)
  - [Pipeline](#pipeline)
  - [Setting up your Jetson](./doc/jetson-setup.md)
  - [Vienamese Plate Dataset](./doc/dataset.md)
  - [License PLate Detection](./doc/plate-detect.md)
  - [License Plate Recognition](./doc/plate-ocr.md)
  - [Trained Models](#trained-models)
  - [Reference](#reference)

## Pipeline

This project is developed based on the pipeline described below. From a set of data collected in practice to the problem you want to solve. For details in this project, we will use the dataset of Vietnamese license plates.

<div align='center'>
  <img src="./doc/images/from-colab-to-jetson.png" width="95%">
</div>

First, you need to prepare a labeled dataset. Then train the object detection model with the GPU on [Google Colab](https://colab.research.google.com/ "Google Colab") or your computer. Depending on the Deeplearning Framework you use, it will output the model file in different formats. With ONNX you can convert most of the above formats to a single `.onnx` format. Then with [TensorRT](https://developer.nvidia.com/tensorrt "TensorRT") installed on the [Jetpack Jetson Nano](https://developer.nvidia.com/embedded/jetpack "Jetpack"), you can run the object detection algorithms with high accuracy and FPS.

## Setting up your Jetson

To get started with this project you need to install your jetson nano with the libraries and source code as follows:

* [Setting up your Jetson](./doc/jetson-setup.md)

## Vienamese Plate Dataset
The project shares two sets of data for the license plate identification problem in Vietnam:

* [Vienamese Plate Dataset](./doc/dataset.md)

* [License PLate Detection Dataset](https://drive.google.com/file/d/1KLK-DWgT3VoQH4fcTxAt2eB3sm7DGWAf/view?usp=sharing "plate dataset")

* [License Plate Recognition Dataset](https://drive.google.com/file/d/1Mdtfn39Jt53u9Y81jhoM-7pdQT7B_dF6/view?usp=sharing "ocr dataset")
          
## License PLate Detection

License PLate Detection results with `40 FPS` on Jetson Nano:

<div align='center'>
  <img src="./doc/images/plate_result2.gif" width="60%">
</div>

License Plate Detection tutorial:

* [License Plate Detection](./doc/plate-detect.md)

## License Plate Recognition

License Plate Recognition results with `40 FPS` on Jetson Nano:

<div align='center'>
  <img src="./doc/images/ocr_result2.gif" width="60%">
</div>

License Plate Recognition tutorial:

* [License Plate Recognition](./doc/plate-ocr.md)

## Trained Models

 **1. License PLate Detection:**

|Network         |FPS |num_class|Model| 
|----------------|----|---------|-----|
|SSD-Mobilenet-v1|40  |1        |[link](https://drive.google.com/file/d/1eBO1UzZkp4pa5b966Un1oBwccdtt5ID_/view?usp=sharing)|
|YoloV4          |None|1        |[link](https://drive.google.com/file/d/1eG0ccO0HvberUiesS380zQNTJM3eHn_m/view?usp=sharing)|
|YoloV4-tiny     |None|1        |[link](https://drive.google.com/file/d/1ZLno2-e7yXnJs0wo9tVXq7bvqT-9Jawm/view?usp=sharing)|
|Wpod            |10  |1        |[link](https://drive.google.com/file/d/1pUHHPu31QQittRnKIXRmhAe1j-diCv1N/view?usp=sharing)|

**2. License Plate Recognition:**

|Network         |FPS |num_class|Model| 
|----------------|----|---------|-----|
|SSD-Mobilenet-v1|40  |36       |[link](https://drive.google.com/file/d/1wTTWONFUXRBtSKA-Cq3snL21KXCB80PS/view?usp=sharing)|
|SVM             |None|36       |[link](https://drive.google.com/file/d/1rmQi7NwKAeunvmB8dF_SUi2JVEmRop4g/view?usp=sharing)|

## Reference

```
[1] https://github.com/dusty-nv/jetson-inference
[2] Liu, Wei, et al. "Ssd: Single shot multibox detector." European conference on computer vision. Springer, Cham, 2016.
[3] Howard, Andrew G., et al. "Mobilenets: Efficient convolutional neural networks for mobile vision applications." arXiv preprint arXiv:1704.04861 (2017).
[4] Bochkovskiy, Alexey, Chien-Yao Wang, and Hong-Yuan Mark Liao. "YOLOv4: Optimal Speed and Accuracy of Object Detection." arXiv preprint arXiv:2004.10934 (2020).
```
