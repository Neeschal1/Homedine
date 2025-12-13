from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('createandlistproducts/', views.ProductsSerializersListCreateAPIViews.as_view(), name='ProductsSerializersListCreateAPIViews'),
    path('modifyproduct/<int:pk>/', views.ProductsSerializersRetrieveUpdateDestroyViews.as_view(), name='ProductsSerializersRetrieveUpdateDestroyViews')
]
