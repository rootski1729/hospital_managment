"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import *
from patients.views import *
from doctors.views import *

from mappings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    
    # Patients URLs
    path('api/patients/', PatientListCreateView.as_view()),
    path('api/patients/<int:pk>/',PatientDetailView.as_view()),
    
    # Doctors URLs
    path('api/doctors/', DoctorListCreateView.as_view()),
    path('api/doctors/<int:pk>/', DoctorDetailView.as_view()),
    
    # Mappings URLs
    path('api/mappings/', MappingListCreateView.as_view()),
    path('api/mappings/<int:patient_id>/',MappingDetailView.as_view()),
    path('api/mappings/delete/<int:pk>/',MappingDeleteView.as_view()),

]
