from django.contrib import admin
from django.urls import path,include
from .views import *
from .models import Student


urlpatterns = [
    # path('',home),
    path('student/',StudentAPI.as_view()),
    # path('update-student/<id>/',update_student,name = "update-student"),
    # path('delete-student/<id>/',delete_student,name = "delete-student"),
    path('get-book/',get_book,name = "get-book"),
    path('register/',Registeruser.as_view()),
    path('generic-student/',Studentgeneric.as_view()),
    path('generic-student/<id>/',Studentgeneric1.as_view()),
    path('pdf/', Generatepdf.as_view()),
    path('excel/', importexportExcel.as_view()),

]
