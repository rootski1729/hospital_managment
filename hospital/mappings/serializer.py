from .models import patientDoctorMapping
from rest_framework import serializers

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = patientDoctorMapping
        fields = '__all__'
        
        