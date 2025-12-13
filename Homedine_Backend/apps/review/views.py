from django.shortcuts import render
from django.http import HttpResponse

def userreviewhome(request):
    return HttpResponse("Welcome! This is the default user review setup.")