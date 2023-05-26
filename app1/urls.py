from django.urls import path
from app1.views import *
#from app1.views import *
app_name = 'good'

urlpatterns = [
    path('vk/',vk,name='vk'),
    path('ab/',ab,name='ab'),
]