from django.contrib import admin
from .models import Data, ProcessedData


class DataAdmin(admin.ModelAdmin):
    pass


class ProcessedDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Data, DataAdmin)
admin.site.register(ProcessedData, ProcessedDataAdmin)