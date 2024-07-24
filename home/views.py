from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .models import *
from  .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from home.serializers import Userserializer
import datetime
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .helpers import *
import pandas as pd 
from django.conf import settings
import uuid
# Create your views here.


class importexportExcel(APIView):
    def get(self,request):
        student_obj = Student.objects.all()
        serializer = Studentserializer(student_obj, many = True )
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv",encoding="UTF-8",index = False)
        return Response({
            'status':200
        })
    
    def post(self,request):
        excel_upload_obj = Excelfileupload.objects.create(excel_file = request.FILES['files'])
        df = pd.read_csv(f"{settings.BASE_DIR}/public/static/{excel_upload_obj.excel_file}")
        for student in (df.values.tolist()):
            print(student)
        return Response({'status':200})





class Generatepdf(APIView):
    def get(self,request):
        student_obj = Student.objects.all()
        params = {
            'today': datetime.date.today(),
            'student_obj':student_obj,
        }
        file_name , status = save_pdf(params)
        if not status:
            return Response({
                'status': 400,

            })
        return Response({'status':200, 'path' : f'/media{file_name}.pdf' })

class Studentgeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer


class Studentgeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    lookup_field = 'id'





@api_view(['get'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = Bookserializer(book_obj, many = True)
    return Response({'status':200,'payload':serializer.data})

class Registeruser(APIView):
    def post(self,request):
        serializer = Userserializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors,'message':'Something Went Wrong!!'})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,
                         'payload':serializer.data,
                         'refresh': str(refresh),
                         'access': str(refresh.access_token),
                         'message':'Hello'})

class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # def get(self,request):
    #         student_obj = Student.objects.all()
    #         serializer = Studentserializer(student_obj, many = True)
    #         return Response({'status':200,'payload':serializer.data})
    

    # def post(self,request):
    #     serializer = Studentserializer(data = request.data)
    #     if not serializer.is_valid():
    #         print(serializer.errors)
    #         return Response({'status':403, 'errors':serializer.errors,'message':'Something Went Wrong!!'})
    #     serializer.save()
    #     return Response({'status':200,'payload':serializer.data,'message':'Hello'})
    

    # def put(self,request):
    #     try:
    #         student_obj = Student.objects.get(id = request.data['id'])
    #         serializer = Studentserializer(student_obj,data = request.data, partial = False)
    #         if not serializer.is_valid():
    #             print(serializer.errors)
    #             return Response({'status':403, 'errors':serializer.errors,'message':'Something Went Wrong!!'})
    #         serializer.save()
    #         return Response({'status':200,'payload':serializer.data,'message':'Hello'})
    
    #     except Exception as e:
    #         return Response({'status':403,'message':'Invalid ID'})
        
        
    # def patch(self,request):
        
    #     try:
    #         student_obj = Student.objects.get(id = request.data['id'])
    #         serializer = Studentserializer(student_obj,data = request.data, partial = True)
    #         if not serializer.is_valid():
    #             print(serializer.errors)
    #             return Response({'status':403, 'errors':serializer.errors,'message':'Something Went Wrong!!'})
    #         serializer.save()
    #         return Response({'status':200,'payload':serializer.data,'message':'Hello'})
    
    #     except Exception as e:
    #         return Response({'status':403,'message':'Invalid ID'})
        

    # def delete(self,request):
    #         try:
    #             student_obj = Student.objects.get(id = request.data['id'])
    #             student_obj.delete()
    #             return Response({'status':200,'message':'Deleted successfully'})
            
    #         except Exception as e:
    #             return Response({'status':403,'message':'Invalid ID'})








# @api_view(['get'])
# def home(request):


# @api_view(['post'])
# def post_student(request):
    


# @api_view(['put','patch'])
# def update_student(request,id):

    
# @api_view(['delete'])
# def delete_student(request,id):
