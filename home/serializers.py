from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        #fields = ['name','age']
        #exclude = ['id',]
        fields = '__all__'

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class Bookserializer(serializers.ModelSerializer):
    category = Categoryserializer()
    class Meta:
        model = Book
        fields = '__all__'