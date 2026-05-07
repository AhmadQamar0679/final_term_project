from django.urls import path
from . import views


urlpatterns = [
    path('',views.doctor_details,name='doctor_page')
]
