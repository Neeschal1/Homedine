from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi, This is the default page of Homedine Backend Page. Welcome :)")