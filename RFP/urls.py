from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.rfp_project_list, name="projects"),
    path('project/update/<int:id>/', views.rfp_update, name="rfp_update"),
    path('project/freeze/<int:id>/', views.rfp_remove, name="rfp_delete"),
]