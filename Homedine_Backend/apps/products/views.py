from django.shortcuts import render
from django.http import HttpResponse

def products(request):
    return HttpResponse("This is Products Default Backend Page. Welcome :)")