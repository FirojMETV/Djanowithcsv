# csv_upload/models.py
from django.db import models

class DynamicModel(models.Model):
    # name = models.CharField(max_length=255)
    # description= models.TextField()
    pass  # Your static model fields can be defined here

class DynamicData(models.Model):
    dynamic_model = models.ForeignKey(DynamicModel, on_delete=models.CASCADE)
    
    column_name = models.CharField(max_length=255)
    column_value = models.CharField(max_length=255)
