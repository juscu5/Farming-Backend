from django.urls import path
from . import views

urlpatterns = [
    path('', views.workload, name="workload"),
    path('<int:id>/', views.update_comments, name="update_comments"),
   
]