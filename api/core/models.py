from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

############### LEARN VIEW #######################


class Data(models.Model):
    """Комментарии"""
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to="learnVue/post_image/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data_user', default=1)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def create_processed_data(self):
        """Создает запись в обработанных данные"""
        ProcessedData.objects.create(img=self.img, data=self)

class ProcessedData(models.Model):
    """Комментарии"""

    img = models.ImageField(upload_to="learnVue/post_image/")
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='processed_data_data')

    def __str__(self):
        return str(self.id)


class TestFile(models.Model):
    file = models.FileField(upload_to="learnVue/file/")

    def __str__(self):
        return str(self.id)