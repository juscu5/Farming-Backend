from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users, name="get_users"),
    path('create/', views.create_user, name="create_users"),
    path('update/', views.update_user, name="update_users"),
    path('freeze/<str:pk>/', views.freeze_user, name="freeze_users"),
    path('freeze/', views.delete_user, name="delete_users"),
    path('employee/', views.get_employee, name="get_employee"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('rehydrate/', views.rehydrate_user_info, name='rehydrate_user_info'),
]