from django.shortcuts import render
from django.http import HttpResponse

def userhome(request):
    return HttpResponse("This is User Verification Defaule Backend Page. Welcome :)")