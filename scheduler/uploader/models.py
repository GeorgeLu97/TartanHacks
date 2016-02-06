from django.db import models

# Create your models here.
class FileUpload(models.Model):
    upload = models.FileField(upload_to="./uploads/%Y/%M/%d")