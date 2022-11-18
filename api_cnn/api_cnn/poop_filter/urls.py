from django.contrib import admin
from django.urls import path, include

from .views import GetLabelView

urlpatterns = [
    path("poop/", GetLabelView.as_view())
]
