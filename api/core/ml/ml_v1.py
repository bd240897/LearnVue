# -*- coding: utf-8 -*-
"""Копия блокнота "try load data and predict.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TxQtoRW01D2Pw4P8iTtmIfQl4ZAmGZ0x

# Финал
"""

import torch.nn as nn
import torch
from sklearn.preprocessing import LabelEncoder
from torchvision import transforms
from PIL import Image
import pickle
from pathlib import Path
from os.path import basename
import json
import numpy as np

# 1. КОНСТАНТЫ

# обработка
RESCALE_SIZE = 224

# модель
N_CLASSES = 42

# загрузки
PATH_MODEL = "../ml_static/model_weights.pth"
PATH_LABEL_ENCODER = "../ml_static/label_encoder.pkl"
PATH_LABELS_LIST = "../ml_static/labels.json"

# картинка
# пусть до картинки
PATH_IMG_FILE = "../ml_static/data/agnes_skinner/pic_0000.jpg"
# метка по названию папки
correct_label = basename(Path(PATH_IMG_FILE).parent)

# 2. ОБРАБОТКА ДАННЫХ (функции)

def load_sample(file):
    """Загружаем изображения"""
    image = Image.open(file)
    image.load()
    return image

def do_resize(image):
    """Изменяем размер изображения"""
    image = image.resize((RESCALE_SIZE, RESCALE_SIZE))
    return np.array(image)

def do_transform(file):
    # для преобразования изображений в тензоры PyTorch и нормализации входа
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) 
    ])

    x = load_sample(file)
    x = do_resize(x)
    x = np.array(x / 255, dtype='float32')
    x = transform(x)
    return x

# 3. СТРУКТУРА СЕТИ (класс)

class SimpleCnn(nn.Module):

    def __init__(self, n_classes):
        super().__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.conv5 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=96, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.out = nn.Linear(96 * 5 * 5, n_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)

        x = x.view(x.size(0), -1)
        logits = self.out(x)
        return logits

# 4. ПРЕДСКАЗАНИЕ ОДНОЙ КАРТИНКИ (функции)

def predict_one_sample(model, inputs):
    """Предсказание, для одной картинки"""

    with torch.no_grad():
        inputs = inputs
        model.eval()
        logit = model(inputs)
        probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
    return probs

# 5. ЗАГРУЗКА МОДЕЛИ ()


def make_prediction(file=PATH_IMG_FILE):
    """Подгрузить модели и сделать предсказание"""

    # загрузка модели
    model = SimpleCnn(n_classes=N_CLASSES)
    model.load_state_dict(torch.load(PATH_MODEL, map_location=torch.device('cpu')))
    model.eval()  # model.train() - это переключатель

    # загурзка кодирования лейблов
    label_encoder = pickle.load(open(PATH_LABEL_ENCODER, 'rb'))

    # загрузка списка меток
    with open(PATH_LABELS_LIST, 'r') as f:
        labels_list = json.load(f)

    # 6. ДЕЙСТВИЯ

    # обработка исходных данных
    one_pearson = do_transform(file=file)
    # предсказание модели
    probs_im = predict_one_sample(model, one_pearson.unsqueeze(0))
    # выбор индекса максимального аругменты
    id_y_pred = np.argmax(probs_im)
    # определение имени предсказанного класса класса
    y_pred = label_encoder.classes_[id_y_pred]
    print(y_pred)
    return y_pred


if __name__ == '__main__':
    user_file = r"C:\Users\Дмитрий\WebstormProjects\LearnVue\api\media\third_img.jpg"
    make_prediction(file=user_file)