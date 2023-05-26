from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def second_ap2(request):
    return HttpResponse("this is an second app apllication!!!!!!....")


def dhoni(request):
    return HttpResponse ("Dhoni is a good Finisherr...!!!!!!")