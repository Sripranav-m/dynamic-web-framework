from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

import os


class Formdata(models.Model):
    username=models.CharField(max_length=100,default="")
    code=models.TextField()
    def __str__(self):
        return self.username

class Menu(models.Model):
    mycode=models.TextField()
    username=models.CharField(max_length=100,default="")
    num=models.IntegerField(default=1)
    displaycode=models.TextField(max_length=10000)
    displaycss=models.TextField()
    displayjs=models.TextField()
    navbarcode=models.TextField()
    def __str__(self):
        return self.username
class content_for_Menu(models.Model):
    username=models.CharField(max_length=100,default="")
    content=RichTextUploadingField(blank=True,null=True)
    name=models.CharField(max_length=100,default="")
    def __str__(self):
        return (self.username+"->"+self.name)
class carousel_Image(models.Model):
    username=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='images/') 
    def __str__(self):
        return (self.username+"->"+self.name)