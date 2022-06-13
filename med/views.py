from django.shortcuts import render
from .models import Doctors

# Create your views here.
def index(request):
    return render(request, 'index.html')

def LabTest(request):
    
    return render(request, 'LabTest.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def DoctorDetails(request):
    Docs=Doctors.objects.all()
    return render(request, 'DoctorDetails.html',{'Docs' : Docs})
