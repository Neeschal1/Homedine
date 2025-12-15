from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome, name='userhome'),
    path('createaccount/', views.UserAccountSignupSerializersListCreateAPIView.as_view(),name='UserAccountSignupSerializersListCreateAPIView'),
    path('modifyaccount/<int:pk>/', views.UserAccountSignupSerializersRetrieveUpdateDestroyAPIView.as_view(), name='UserAccountSignupSerializersRetrieveUpdateDestroyAPIView'),
    path('createaccount/otp/', views.UserOTPVerificationSerializersView.as_view(), name='UserOTPVerificationSerializersView'),
    path('login/', views.UserLoginSerializersView.as_view(), name='UserLoginSerializersView'),
]

