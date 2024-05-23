from django.urls import path
from . import views

urlpatterns = [
     path('', views.costsavings, name="costsavings"),
     path('create/', views.costsavings_create, name="create"),
    
     path('<int:id>/', views.costsavings_update, name="update"),
     path('remove/<int:id>/', views.costsavings_delete, name="delete"),

     #  path('quarter/',views.ph_farming_savings_api, name='ph_farming_savings_api'),

     #  path('quarter/',views.farming_savings_quarters, name='ph_farming_savings_api'),
      # path('quarter/',views.ph_farming_savings, name='ph_farming_savings_api'),
]