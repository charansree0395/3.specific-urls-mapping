from django.urls import path
from app2.views import *

app_name ='app2'
 
urlpatterns = [
    path('second_ap2/',second_ap2,name='second_ap2'),
]