# Object Detection And Tracking

One-line version: a combined computer vision repo for YOLOv11 object detection practice and OpenCV object tracking experiments.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/YOLOv11-111827?style=for-the-badge" alt="YOLOv11">
  <img src="https://img.shields.io/badge/Ultralytics-111F68?style=for-the-badge" alt="Ultralytics">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/object--tracking-059669?style=for-the-badge" alt="Object tracking">
</p>

<p align="center">
  <img src="assets/tracking-demo.gif" alt="Object tracking animation" width="760">
</p>

## What It Does

This repo keeps two related computer vision practice areas together:

- object detection with YOLOv11 notebooks
- object tracking with OpenCV tracker scripts

Useful because detection answers "what is in the frame?" and tracking answers "where did it go next?" Basically, the camera version of keeping an eye on things without looking suspicious.

## Practice Preview

<p align="center">
  <img src="assets/yolo-output.png" alt="YOLO notebook output" width="720">
</p>

## Topics And Files

| Topic | File |
| --- | --- |
| Getting started with YOLOv11 object detection | `notebooks/object_detection/Getting_Started_with_Yolov11__Object_Detection.ipynb` |
| Custom dataset training with YOLOv11 | `notebooks/object_detection/Custom_Dataset_Training_with_YOLOv11.ipynb` |
| BOOSTING tracker | `tracking/opencv_trackers/boosting.py` |
| CSRT tracker | `tracking/opencv_trackers/csrt.py` |
| GOTURN tracker script | `tracking/opencv_trackers/goturn.py` |
| KCF tracker | `tracking/opencv_trackers/kcf.py` |
| MEDIANFLOW tracker | `tracking/opencv_trackers/medianflow.py` |
| MIL tracker | `tracking/opencv_trackers/mil.py` |
| MOSSE tracker | `tracking/opencv_trackers/mosse.py` |
| TLD tracker | `tracking/opencv_trackers/tld.py` |

## Quick Start

```bash
pip install -r tracking/opencv_trackers/requirements.txt
pip install ultralytics jupyter
jupyter notebook
```

Open the YOLO notebooks from `notebooks/object_detection/`.

For tracking scripts, run one of the OpenCV tracker files:

```bash
python tracking/opencv_trackers/kcf.py
```

Some trackers may need OpenCV contrib support. If OpenCV complains, it is probably asking for `opencv-contrib-python`, not emotional support. Though honestly, both help.

## Links

- Repo: https://github.com/Siddharth-k7/Object-detection-and-tracking
- Ultralytics docs: https://docs.ultralytics.com/
- OpenCV tracking docs: https://docs.opencv.org/
- Live demo: not hosted; the notebooks and README preview show the practice outputs.

