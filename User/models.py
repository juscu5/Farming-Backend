from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login_id = models.CharField(max_length=30, null=False, unique=True)
    ccms_id = models.IntegerField()
    employee_full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    user_role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    USERNAME_FIELD = "login_id"
    REQUIRED_FIELDS = ["username", "ccms_id", "email", "employee_full_name", "user_role"]

class CCMS(models.Model):
    employee_ident = models.IntegerField()
    employee_common_name = models.CharField(max_length=150)
    login_id = models.CharField(max_length=50)
    email1 = models.CharField(max_length=100)
    ccms_current_position = models.CharField(max_length=50)
    ccms_current_status = models.CharField(max_length=20)
    inserted_date_time_ph = models.DateTimeField(null=True)
    updated_date_time_ph = models.DateTimeField(null=True)
    class Meta:
        db_table = 'CCMS_Employee'

class AuthLogs(models.Model):
    login_id = models.CharField(max_length=30)
    inserted_date_time_ph = models.DateTimeField()
    class Meta:
        db_table = 'phf_authlogs'