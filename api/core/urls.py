from django.urls import path, include
from .views import UploadView, ReceiveDataView, RequestListView, TestView



# роуты api
urlpatterns_api = [path("upload/", UploadView.as_view()),
                   path("receive/source/", ReceiveDataView.as_view()),
                   path("receive/processed/", ReceiveDataView.as_view()),
                   path("list/", RequestListView.as_view()),
                   path("test/", TestView.as_view()),
                   ]


urlpatterns = [path("", include(urlpatterns_api)),

               ]