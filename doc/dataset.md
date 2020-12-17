<img src="./images/githubtitle.png" width="100%">

# Vienamese Plate Dataset
## Introduction

Vietnamese Plate Dataset is a data set of number plates of vehicles in Vietnam. This data set is divided into two small datasets with separate tasks for the problem of identifying license plates in Vietnam.

## License PLate Detection Dataset

License PLate Detection Dataset is a data set used to train the model to detect license plates in the image. The detected license plate will be used to read the characters in the plate in the next step.

<div align='center'>
    <img src="./images/plate_dataset.png" width="80%">
</div>

The data set is provided in two formats, VOC / PASCAl and YOLO. The download link is in the table below:

| Dataset| VOC | YOLO |
|--------|-----|------|
|Vietnamese License Plate Detection|[link](https://drive.google.com/file/d/1irJC4V4IlxJJKOtJX1u0LZSSUrKjjgTq/view?usp=sharing "plate voc")|[link](https://drive.google.com/file/d/1KLK-DWgT3VoQH4fcTxAt2eB3sm7DGWAf/view?usp=sharing "plate yolo")|

Some videos of street scenes in Vietnam are used to check the performance  of the model.
| Video| Download |
|--------|-----|
|      test  | [link](https://drive.google.com/drive/folders/1XXpHaRq5VPIR7lQoOEg9X76LbZDzFals?usp=sharing "test video")      |
## License Plate Recognition Dataset

License Plate Recognition Dataset is a data set used to train algorithms to detect and classify characters in a license plate.

<div align='center'>
    <img src="./images/ocr_dataset.png" width="80%">
</div>

The data set is provided in two formats, VOC / PASCAl and YOLO. The download link is in the table below:

| Dataset| VOC | YOLO |
|--------|-----|------|
|Vietnamese License Plate Recognition|[link](https://drive.google.com/file/d/1-k-8H1owJnijj_1ymGJFxs0UYjfAvogg/view?usp=sharing "ocr voc")|[link](https://drive.google.com/file/d/1Mdtfn39Jt53u9Y81jhoM-7pdQT7B_dF6/view?usp=sharing "ocr yolo")|

## Build the Dataset

This project provides snippets of code so you can create your own dataset.

### Crop plate 

1. Add vehicle images with number plates to the "img_in" folder.
2. Run the command below  to proceed to separate the license plate from the image. The extracted number plate image will save in "img_out" folder.

> Note: Choose one of the two.

*Use [YoloV4 tiny model]() (faster):*

```python
python3 .\yolo_folder.py -f ./img_in/ -o ./img_out/ -cl ./data/obj.names -w ./backup/yolov4-tiny-obj_best.weights -c ./cfg/yolov4-tiny-obj.cfg

```

*Use [YoloV4 model]() (high accuracy):*

```python
python3 .\yolo_folder.py -f ./img_in/ -o ./img_out/ -cl ./data/yolov4-obj.names -w ./backup/yolov4-obj_best.weights -c ./cfg/yolov4-obj.cfg
```

### Pre-processing

1. Convert lables format ([original source](https://github.com/hai-h-nguyen/Yolo2Pascal-annotation-conversion))

```python
python3 yolo2voc.py ./dataset
```

2. Data augmentation

```python
python3 gendata.py
```

3. Split dataset

```python
python3 splitdata.py
```

4. Resize

```python
python3 resize.py
```

## Reference

Thanks [Mì Ai](https://www.miai.vn/) for sharing a part in this dataset. You can download more type datasets [here](https://www.miai.vn/thu-vien-mi-ai/).