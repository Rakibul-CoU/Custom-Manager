from django.shortcuts import render

from api.models import Hospital
from django.views.generic import ListView

# Create your views here.


class HospitalListView(ListView):
    model = Hospital
    template_name = 'hospital_list.html'
    context_object_name = 'hospitals'
    
    def get_queryset(self):
        result = Hospital.dhaka_hospitals.all()
        return result
    


class HospitalListViewArgument(ListView):
    model = Hospital
    template_name = 'hospital_list.html'
    context_object_name = 'hospitals'
    
    def get_queryset(self):
        city = self.kwargs['city']
        result = Hospital.dhaka_hospitals_arg.all(city)
        return result
    
class AllHospitalListView(ListView):
    model = Hospital
    template_name = 'hospital_list.html'
    context_object_name = 'hospitals'
    
    def get_queryset(self):
        result = Hospital.all_hospitals.get_all_hospitals()
        print(result)
        return result
    
    

    
