from django.contrib import admin

# Register your models here.

from .models import Hospital

class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

admin.site.register(Hospital, HospitalAdmin)
