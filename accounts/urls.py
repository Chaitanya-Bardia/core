from django.contrib import admin
from django.urls import path,include
from .views import *
from .views import *


urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('verifyotp/',verifyotp.as_view()),
    path('verifyemail/',verifyemail.as_view()),
]