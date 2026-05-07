from django.shortcuts import render

# Create your views here.

def doctor_details(request):
    return render(request,'doctors_info.html')
