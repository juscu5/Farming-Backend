from rest_framework import serializers
from SubmitForm.models import PH_Farming_Solution

class Dashboard_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PH_Farming_Solution 
        fields = ( 'farming_ident', 'client_ref_id','type_ref','sites_ref','client_ref','user_ref'
                  ,'count','target_date' 
                  ,'critical_item','status','is_active')

class Dashboard_Serializer2(serializers.ModelSerializer):
    class Meta:
        model = PH_Farming_Solution 
        fields = ( 'farming_ident', 'type_ref','sites_ref','client_ref','user_ref'
                  ,'count','target_date')
