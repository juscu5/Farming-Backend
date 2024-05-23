from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.list_dashboard, name="dashboard"), 
    path('projects/', views.list_all_serializer, name="projects"),
]
