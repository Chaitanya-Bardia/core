from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

class Excelfileupload(models.Model):
    excel_file = models.FileField(upload_to="excel")


