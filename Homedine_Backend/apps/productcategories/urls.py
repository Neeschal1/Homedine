from django.urls import path
from . import views

urlpatterns = [
    path('', views.productcategories, name='productcategories')
]
