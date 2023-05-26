from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vk(request):
    return HttpResponse("This vk belons to india")
def ab(request):
    return HttpResponse("This is AB belongs to SouthAfrica")