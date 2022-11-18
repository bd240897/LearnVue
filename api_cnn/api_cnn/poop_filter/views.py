from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response

from .ml_alexnet.BaselineClass import BaseLine
from PIL import Image

class GetLabelView(View):
    def get(self, request, *args, **kwargs):
        IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
        IMG_URL = "https://i.ytimg.com/vi/IzbSy7LrnjE/maxresdefault.jpg"
        model = BaseLine()
        prediction = model.predict_file(url=IMG_URL)
        return HttpResponse(f"prediction is {prediction}")


class GetLabelView(generics.GenericAPIView):

    def get(self, request, *args,  **kwargs):
        # IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
        # IMG_URL = "https://i.ytimg.com/vi/IzbSy7LrnjE/maxresdefault.jpg"

        url = request.GET.get('url')
        if not url:
            return Response("Вы не передали URL картинки!", status=status.HTTP_400_BAD_REQUEST)

        try:
            model = BaseLine()
            prediction = model.predict_file(url=url)
            print(prediction)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response({"prediction": prediction})