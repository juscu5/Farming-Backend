from rest_framework import serializers
from SubmitForm.models import Farming_Solution_User,Farming_Solution_Client,Farming_Solution_Type,Farming_Solution_Sites,PH_Farming_Solution,PH_Farming_Action_Logs


class Farming_Solution_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farming_Solution_User
        fields = ('user_id','ccms_id','first_name','middle_name','last_name','ccms_uname','user_type')
 
class Farming_Solution_Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farming_Solution_Client
        fields =('client_id', 'client_name', 'project_name')

class Farming_Solution_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farming_Solution_Type
        fields = ('type_id', 'type_name')

class Farming_Solution_Sites_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farming_Solution_Sites
        fields = ('site_id', 'site_name')

class Tracker_Farming_Solution_Serializer(serializers.ModelSerializer):
    user_ref = Farming_Solution_User_Serializer()
    client_ref = Farming_Solution_Client_Serializer()
    type_ref = Farming_Solution_Type_Serializer()
    sites_ref = Farming_Solution_Sites_Serializer()

    class Meta:
        model = PH_Farming_Solution
        fields = ("farming_ident", "seat_req",
        "need",  "count",  "requested_date",  "target_date",
        "resolved_date", "resolved_days", "critical_item", "status",
        "remarks", "solution", "email_trail", 
        "created_dt_utc", "is_active",
        "client_ref", "sites_ref", "type_ref",  "user_ref")

class Tracker_Farming_Solution_Custom_Serializer(serializers.ModelSerializer):
    type_ref = serializers.IntegerField(source='type_ref_id')
    sites_ref = serializers.IntegerField(source='sites_ref_id')
    client_ref = serializers.IntegerField(source='client_ref_id')
    user_ref = serializers.IntegerField(source='user_ref_id')
    class Meta:
        model = PH_Farming_Solution
        fields = '__all__'

class Tracker_Farming_Solution_Put_Custom_Serializer(serializers.ModelSerializer):
    type_ref = serializers.IntegerField(source='type_ref_id')
    sites_ref = serializers.IntegerField(source='sites_ref_id')
    client_ref = serializers.IntegerField(source='client_ref_id')
    user_ref = serializers.IntegerField(source='user_ref_id')
    class Meta:
        model = PH_Farming_Solution
        # fields = '__all__'
        fields = ("farming_ident", "seat_req",
        "need",  "count",  "requested_date",  "target_date",
        "resolved_date", "resolved_days", "critical_item", "status",
        "remarks", "solution", "email_trail",
       "updated_dt_utc", "is_active",
        "client_ref", "sites_ref", "type_ref",  "user_ref")

class Tracker_Farming_Solution_delete_Custom_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PH_Farming_Solution
        fields = 'farming_ident', 'is_active', #"updated_dt_utc"

class PHF_Action_Logs_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PH_Farming_Action_Logs
        fields = ('id_ref','action','page','inserted_by','inserted_date_time_ph')