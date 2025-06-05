from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permission import IsAdminUser
from .models import Doctor

from .serializers import DoctorSerializer
# Create your views here.

class DoctorListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated, IsAdminUser]
    
    def post(self, request):
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Doctor created successfully", "doctor": serializer.data}, status=status.HTTP_201_CREATED)
            
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request):
        try:
            doctors = Doctor.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response({"doctors": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class DoctorDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request, pk):
        try:
            doctor= Doctor.objects.get(pk=pk, is_deleted=False)
            serializer = DoctorSerializer(doctor)
            return Response({"doctor": serializer.data}, status=status.HTTP_200_OK)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk, is_deleted=False)
            serializer= DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Doctor updated successfully", "doctor": serializer.data}, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            doctor = Doctor.objects.get(pk=pk,is_deleted=False)
            doctor.is_deleted = True
            return Response({"message": "Doctor deleted successfully"}, status=status.HTTP_200_OK)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        