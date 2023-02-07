from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('kilometers/', views.getKilometers, name="kilometers"),
    path('kilometers/<str:pk>/', views.getKilometer, name="kilometer"),
    path('updateKilometers/', views.updateKilometers, name="updateKilometers"),
    #path('oauth2/', views.setAuthtoken, name="authtoken")
]
