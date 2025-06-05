from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permission import IsAdminUser

from .models import patientDoctorMapping
from .serializer import MappingSerializer

from rest_framework import status
# Create your views here.


class MappingListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        try:
            mappings = patientDoctorMapping.objects.all()
            serializer = MappingSerializer(mappings, many=True)
            return Response({"mappings": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer= MappingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Mapping created successfully", "mapping": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MappingDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def delete(self, request, pk):
        try:
            mapping = patientDoctorMapping.objects.get(pk=pk, is_deleted=False)
            mapping.is_deleted = True
            mapping.save()
            return Response({"message": "Doctor deleted from patient successfully"}, status=status.HTTP_204_NO_CONTENT) 
        except patientDoctorMapping.DoesNotExist:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class MappingDetailView(APIView):
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticated, IsAdminUser]
    
    def get(self, request, patient_id):
        try:
            mappings = patientDoctorMapping.objects.filter(patient_id=patient_id, is_deleted=False)
            serializer = MappingSerializer(mappings, many=True)
            return Response({"mappings": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)