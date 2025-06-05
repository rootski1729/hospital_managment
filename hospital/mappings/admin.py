from django.contrib import admin
from .models import patientDoctorMapping
# Register your models here.

@admin.register(patientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'is_deleted')
    ordering = ('appointment_date',)  