from django.shortcuts import render

# Create your views here.

def client_home(request):
    return render(request,'client_side._home.html')
