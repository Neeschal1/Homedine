from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('userverification/', include('apps.userverification.urls')),
    path('products/', include('apps.products.urls')),
]
