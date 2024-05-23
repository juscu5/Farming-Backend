from rest_framework import serializers 
from .models import User, CCMS, AuthLogs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields = (
            'id',
            'login_id',
            'ccms_id', 
            'employee_full_name',
            'email',
            'user_role',
            'status'
        )

class CcmsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CCMS 
        fields = (
            'employee_ident',
            'employee_common_name', 
            'login_id',
            'email1'
        ) 

class UpdateUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields = ('login_id','user_role') 

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields = ('user_role', 'status') 

class FreezeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields = ('login_id','status') #,'user_role'

class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields = ('login_id','user_role','is_active')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ccms_id', 'login_id', 'email', 'employee_full_name', 'user_role', 'status']

class AuthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthLogs 
        fields = ('login_id', 'inserted_date_time_ph') 