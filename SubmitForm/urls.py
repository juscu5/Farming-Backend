from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_project, name="submit_project"),
    path('sites/', views.list_sites, name="sites"),
    path('sites/<int:id>/', views.get_site, name="site_id"),
    path('site/create/', views.create_site, name="create_site"),
    path('clients/', views.get_clients, name="clients"),
    path('client/<int:id>/', views.get_client, name="client_id"),
    path('client/create/', views.create_client, name="create_client"),
    path('client/update/<int:id>/', views.client_update, name="update_client"),
    path('client/freeze/<int:id>/', views.freeze_client, name="freeze_client"),
    path('types/', views.list_types, name="types"),
    path('users/', views.get_users, name="users"),
    path('user/<int:id>/', views.get_user, name="user_id"),
]
