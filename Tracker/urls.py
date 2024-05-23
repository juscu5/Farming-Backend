from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.tracker_projects, name="tracker_projects"),
    path('project/update/<int:id>/', views.tracker_update, name="tracker_update"),
    path('project/freeze/<int:id>/', views.update_freeze, name="tracker_freeze"),
]