from rest_framework import serializers
from .models import *
from .helpers import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','phone']

    def create(self, validated_data):
        user = User.objects.create(email = validated_data['email'],phone = validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        send_otp(user.phone,user)
        send_otp_mail(user.email,user)
        return user