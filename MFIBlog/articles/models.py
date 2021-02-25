from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Network(models.Model):
    author = models.ForeignKey("auth.user" , on_delete = models.CASCADE , verbose_name = "Yazar")

    title = models.CharField(max_length = 60 , verbose_name = "Başlık" , unique = True)

    summary = models.CharField(max_length = 90 , verbose_name = "Açıklama")
    
    articleImage = models.FileField(upload_to = 'images' , blank = True , null = True , verbose_name = "Fotograf Ekle")    
    
    content =RichTextUploadingField()

    articlesVideo = models.FileField(upload_to = 'videos' , null = True , blank = True)

    createDate = models.DateTimeField(auto_now_add = True , verbose_name = "Oluşturulma Tarihi")
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createDate']


class SoC(models.Model):
    author = models.ForeignKey("auth.user" , on_delete = models.CASCADE , verbose_name = "Yazar")

    title = models.CharField(max_length = 60 , verbose_name = "Başlık" , unique = True)

    summary = models.CharField(max_length = 90 , verbose_name = "Açıklama")
    
    articleImage = models.FileField(upload_to = 'images' , blank = True , null = True , verbose_name = "Fotograf Ekle")    

    content =RichTextUploadingField()

    articlesVideo = models.FileField(upload_to = 'videos' , null = True , blank = True)

    createDate = models.DateTimeField(auto_now_add = True , verbose_name = "Oluşturulma Tarihi")
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createDate']
    

class Forensic(models.Model):
    author = models.ForeignKey("auth.user" , on_delete = models.CASCADE , verbose_name = "Yazar")

    title = models.CharField(max_length = 60 , verbose_name = "Başlık" , unique = True)

    summary = models.CharField(max_length = 90 , verbose_name = "Açıklama")
    
    articleImage = models.FileField(upload_to = 'images' , blank = True , null = True , verbose_name = "Fotograf Ekle")

    content =RichTextUploadingField()

    articlesVideo = models.FileField(upload_to = 'videos' , null = True , blank = True)

    createDate = models.DateTimeField(auto_now_add = True , verbose_name = "Oluşturulma Tarihi")
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createDate']


class karisik(models.Model):
    author = models.ForeignKey("auth.user" , on_delete = models.CASCADE , verbose_name = "Yazar")

    title = models.CharField(max_length = 60 , verbose_name = "Başlık")

    summary = models.CharField(max_length = 90 , verbose_name = "Açıklama" , unique = True)
    
    articleImage = models.FileField(upload_to = 'images' ,  blank = True , null = True ,verbose_name = "Fotograf Ekle")

    content =RichTextUploadingField()

    articlesVideo = models.FileField(upload_to = 'videos' , null = True , blank = True)
    
    createDate = models.DateTimeField(auto_now_add = True , verbose_name = "Oluşturulma Tarihi")
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createDate']




