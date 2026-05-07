from django.shortcuts import render

# Create your views here.
def management_home(request):
    return render(request,'management_side_home.html')