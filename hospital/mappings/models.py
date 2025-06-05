from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class patientDoctorMapping(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.patient} - {self.doctor} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}"