---
title: YOLOv8 Classification Preprocess Infer with onnxruntime - YOLOv8 分类模型用 onnx 推理的前处理
modify date: 2024-07-07
tags: [Python, Deep Learning, YOLO]
head image: /assets/img/covers/codingcover.jpg
abstract: 在使用 YOLOv8 的训练框架完成分类任务的模型训练后，使用 ultralytics 导出 onnx 模型，在其他设备或环境下进行推理时，需要补充 YOLOv8 的分类前处理，确保推理结果和训练结果一致。
---

> Mofify Date: 2024-07-07

# 场景描述

跟随 YOLOv8 推出的是 `ultralytics` 训练和推理框架，可以一行代码实现分类、检测、分割等任务的训练，以及推理和模型导出。

发现在使用默认设置训练分类模型，并使用 `ultralytics` 库将模型 `pt` 权重一键导出为 `onnx` 后，如果不使用 `ultralytics` 加载 `onnx` 权重，而直接在其他没有 `ultralytics` 的环境和设备上用 `onnxruntime` 直接加载权重并推理，会出现推理结果不一致甚至置信度很低的情况。这是缺少 `pt` 权重文件所能表达的前处理信息，没有实现前处理而导致的。需要补充 YOLOv8 自带的前处理。

---

# 解决方案

可以通过对 `pt` 文件的前处理部分解析，或者对 `ultralytics` 库中 YOLO 分类任务的预测部分代码的源码解析（`ultralytics/models/yolo/classify/predict.py`），找到前处理的代码，补充到 `onnxruntime` 推理代码之前即可：

```python
import torchvision.transforms as T
from torchvision.transforms import InterpolationMode

def get_classify_transforms(size: int=224, mean: Tuple[float, float, float]=(0.0, 0.0, 0.0),
                            std: Tuple[float, float, float]=(1.0, 1.0, 1.0),
                            interpolation: InterpolationMode=InterpolationMode.BILINEAR,
                            crop_fraction: float = 1.0) -> T.Compose:
    """
    复现 YOLO 默认的分类预处理
    """
    if isinstance(size, (tuple, list)):
        assert len(size) == 2
        scale_size = tuple(math.floor(x / crop_fraction) for x in size)
    else:
        scale_size = math.floor(size / crop_fraction)
        scale_size = (scale_size, scale_size)

    if scale_size[0] == scale_size[1]:
        tfl = [T.Resize(scale_size[0], interpolation=interpolation)]
    else:
        tfl = [T.Resize(scale_size)]
    tfl += [T.CenterCrop(size)]

    tfl += [
        T.ToTensor(),
        T.Normalize(
            mean=torch.tensor(mean),
            std=torch.tensor(std),
        ),
    ]

    return T.Compose(tfl)

```

---

# 全部代码

## 训练

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="path/to/dataset/", epochs=100, imgsz=640)
```

## 导出为 onnx

```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a custom trained model

# Export the model
model.export(format="onnx")
```

## 预处理 + onnxruntime 推理

```python
"""
本地执行 onnx 推理
"""
from typing import List, Tuple
import cv2
import onnxruntime as ort
from PIL import Image
import math
import torch
import torchvision.transforms as T
from torchvision.transforms import InterpolationMode

WEIGHT_PATH = "path/to/best.onnx"
names = {0: 'cls1', 1: 'cls2', ...}
cuda = True
providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if cuda else ['CPUExecutionProvider']

def get_classify_transforms(size: int=224, mean: Tuple[float, float, float]=(0.0, 0.0, 0.0),
                            std: Tuple[float, float, float]=(1.0, 1.0, 1.0),
                            interpolation: InterpolationMode=InterpolationMode.BILINEAR,
                            crop_fraction: float = 1.0) -> T.Compose:
    """
    复现 YOLO 默认的分类预处理
    """
    if isinstance(size, (tuple, list)):
        assert len(size) == 2
        scale_size = tuple(math.floor(x / crop_fraction) for x in size)
    else:
        scale_size = math.floor(size / crop_fraction)
        scale_size = (scale_size, scale_size)

    if scale_size[0] == scale_size[1]:
        tfl = [T.Resize(scale_size[0], interpolation=interpolation)]
    else:
        tfl = [T.Resize(scale_size)]
    tfl += [T.CenterCrop(size)]

    tfl += [
        T.ToTensor(),
        T.Normalize(
            mean=torch.tensor(mean),
            std=torch.tensor(std),
        ),
    ]

    return T.Compose(tfl)

def infer_res_from_imgpath(img_path: str, transforms: T.Compose, session: ort.InferenceSession) -> Tuple[int, float]:
    """
    从本地图像文件开始执行推理，返回最高分和类别编号
    """
    image = cv2.imread(img_path)
    image = torch.stack([transforms(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))])
    image = image.numpy()

    outname = [i.name for i in session.get_outputs()]  # ['output']
    inname = [i.name for i in session.get_inputs()]  # ['images']
    inp = {inname[0]: image}
    outputs = session.run(outname, inp)[0]
    return int(outputs[0].argmax()), float(outputs[0].max())

```

