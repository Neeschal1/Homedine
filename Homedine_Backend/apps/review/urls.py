from django.urls import path
from . import views

urlpatterns = [
    path('', views.userreviewhome, name='userreviewhome'),
    path('createreview/', views.UserReviewSerializersVListCreateAPIView.as_view(), name='UserReviewSerializersVListCreateAPIView'),
    path('modifyreview/', views.UserReviewSerializersRetrieveUpdateDestroyAPIView.as_view(), name='UserReviewSerializersRetrieveUpdateDestroyAPIView')
]
