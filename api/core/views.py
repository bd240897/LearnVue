import os.path

from numpy import unicode
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image

from .models import Data, ProcessedData
from .serializers import DataSerialiser, ProcessedDataSerialiser

from django.conf import settings

############### LEARN VIEW #######################
# TODO delete

from .ml.ml_v1_1 import make_prediction

class GetPredictionView(generics.GenericAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = [permissions.AllowAny]

    def is_img_extension(self, path:str):
        allowed_img = [".jpg", ]
        image_type = path[-4:].lower()
        if not (image_type in allowed_img):
            return False
        return True

    def get(self, request):

        id = request.GET.get('id')
        if not id:
            return Response(f"You didn't send id", status=status.HTTP_404_NOT_FOUND)

        # получим картинку
        my_img = Data.objects.get(pk=id)
        # получим и обрабоатем путь для картинки
        path_img_dir_raw = my_img.img.url # r"/media/learnVue/post_image/borisov_2.JPG" # my_img.img.url
        split_path = path_img_dir_raw.split("/")
        path_img_dir = os.path.join(*split_path)

        if not self.is_img_extension(path_img_dir):
            return Response(f"This type of image not allowed!", status=status.HTTP_400_BAD_REQUEST)

        # базовый путь директории проекта
        path_base_dir = settings.BASE_DIR # r"C:\Users\Дмитрий\WebstormProjects\LearnVue\api" # settings.BASE_DIR
        # склеим пуить
        path_full_img = os.path.join(path_base_dir, path_img_dir)

        # сделаем предсказение
        prediction = make_prediction(path_full_img)

        return Response({"prediction": str(prediction)}, status=status.HTTP_201_CREATED)


class UploadView(generics.GenericAPIView):
    """Загрузка файлов и описания"""

    parser_class = (FileUploadParser,)
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Получение данных и описания"""

        # парсим запрос
        file = request.data.get('file')
        description = request.data.get('description')
        name = request.data.get('name')

        # если не передали файл в запросе
        if not file:
            raise ParseError("Empty content")

        # проверка формата файла
        try:
            img = Image.open(file)
            img.verify()
        except:
            raise ParseError("Unsupported image type")

        # сохранение файла в БД
        # RequestData.img.save(f.name, f, save=True)
        a = Data(img=file)
        a.save()

        # создание обработанного файла
        a.create_processed_data()

        # если попутно передали описание
        if description:
            a.description = request.data.get('description')
            a.save()

        # если попутно передали описание
        if name:
            a.name = request.data.get('name')
            a.save()

        # ответ - id созданного запроса
        return Response({'id': a.pk}, status=status.HTTP_201_CREATED)


class ReceiveDataView(generics.GenericAPIView):
    """Отправка файлов"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # парсим запрос
        id = request.query_params.get('id')

        # проверки
        if not id:
            return Response(f"You didn't send id", status=status.HTTP_404_NOT_FOUND)
        elif not Data.objects.filter(pk=id).exists():
            return Response(f"File with id = {id} not found!", status=status.HTTP_404_NOT_FOUND)

        request_data = Data.objects.get(pk=id)
        serialized = DataSerialiser(request_data, context={"request": request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class ReceiveProcessedDataView(generics.GenericAPIView):
    """Отправка файлов"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (обработанный)"""

        # парсим запрос
        id = request.query_params.get('id')

        # проверки
        if not id:
            return Response(f"You didn't send id", status=status.HTTP_404_NOT_FOUND)
        elif not ProcessedData.objects.filter(pk=id).exists():
            return Response(f"File with id = {id} not found!", status=status.HTTP_404_NOT_FOUND)

        request_data = ProcessedData.objects.get(pk=id)
        serialized = ProcessedDataSerialiser(request_data, context={"request": request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class RequestListView(generics.ListAPIView):
    """Отправка списка запросов и описания"""

    queryset = Data.objects.all()
    serializer_class = DataSerialiser
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # post_slug = self.kwargs['post_slug'].lower()
        # post = Post.objects.get(slug=post_slug)
        # return Comment.objects.filter(post=post)
        return super().get_queryset()



from django.core.files import File


from .models import TestFile

import numpy as np
from io import StringIO
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
import uuid, base64
from .models import *
from io import BytesIO

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib import pyplot as plt

class TestView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (обработанный)"""

        # построение графика
        x = np.arange(0, np.pi * 3, .1)
        y = np.sin(x)
        plt.plot(x, y)

        # создание потока
        imgdata = BytesIO()
        # запись того что в потоке
        plt.savefig(imgdata, format="png")
        # создание файла с помощью джанги и добавление имена
        content_file = ImageFile(imgdata)
        content_file.name = '1234.png'

        # запись в БД
        a = Data(img=content_file)
        a.save()

        return Response("well done", status=status.HTTP_200_OK)