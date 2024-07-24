from rest_framework.response import Response
from  .models import *
from  .serializers import *
from rest_framework.views import APIView
from .helpers import *


class RegisterView(APIView):
    def post(self,request):
        try:
            serializer = Userserializer(data = request.data)
            if not serializer.is_valid():
                return Response({
                    'status':403,
                    'errors':serializer.errors
                })
            serializer.save()

            return Response({'status':200,'message':'An OTP has been sent to you on your E-Mail account as well as your registered Phone Number'})

        except Exception as e:
            print(e)
            return Response({'status':404,'error':'Something went wrong'})


class verifyotp(APIView):
    def post(self,request):
        try:
            data = request.data

            user_obj = User.objects.get(phone = data.get('phone'))
            otp = data.get('otp')
            if user_obj.otp == otp:
                user_obj.is_phone_verified = True
                user_obj.save()
                return Response({'status':200,'message':'The OTP has been verified'})
            

            return Response({'status':404,'message':'OTP is incorrect'})

        except Exception as e:
            print(e)
            return Response({'status':404,'error':'Something went wrong'})


    def patch(self,request):
        try:
            data = request.data
            user_obj = User.objects.filter(phone = data.get('phone'))
            if not user_obj.exists():
                return Response({'status':404,'error':'User does not exist.'})

            status,time = send_otp(data.get('phone'),user_obj[0])
            if status:
                return Response({'status':200,'message':'New OTP sent'})
            
            return Response({'status':404,'error':f'Try again after a {time} seconds'})



        except Exception as e:
            print(e)
            return Response({'status':404,'error':'Something went wrong'})
        return Response({'status':404,'error':'Something went wrong'})
    

class verifyemail(APIView):
    def post(self,request):
        try:
            data = request.data
            user_obj = User.objects.get(email = data.get('email'))
            otp = data.get('otp')
            if user_obj.otp == otp:
                user_obj.is_email_verified = True
                user_obj.save()
                return Response({'status':200,'message':'The OTP has been verified'})
            

            return Response({'status':404,'message':'OTP is incorrect'})

        except Exception as e:
            print(e)
            return Response({'status':404,'error':'Something went wrong'})
        
    def patch(self,request):
        try:
            data = request.data
            user_obj = User.objects.filter(email = data.get('email'))
            if not user_obj.exists():
                return Response({'status':404,'error':'User does not exist.'})

            status,time = send_otp_mail(data.get('email'),user_obj[0])
            if status:
                return Response({'status':200,'message':'New OTP sent'})
            
            return Response({'status':404,'error':f'Try again after a {time} seconds'})

        except Exception as e:
            print(e)
            return Response({'status':404,'error':'Something went wrong'})
        return Response({'status':404,'error':'Something went wrong'})