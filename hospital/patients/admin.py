from django.contrib import admin
from .models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'address', 'created_at', 'is_deleted')
    search_fields = ('first_name', 'last_name', 'address')
    list_filter = ('is_deleted',)
    ordering = ('-created_at',)
    
    def has_delete_permission(self, request, obj=None):
        return False