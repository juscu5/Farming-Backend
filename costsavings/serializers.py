from rest_framework import serializers
from .models import PH_Farming_CostSavings #,Farming_Solution_Savings_Accounts #from model(cost_savings) ###, Farming_Solution_Sites
#, Farming_Solution_Savings_Quarter
from SubmitForm.models import Farming_Solution_Sites

#as is
class Farming_Solution_CostSavings_Serializer(serializers.ModelSerializer): ####
    class Meta:
        model = PH_Farming_CostSavings
        fields = ('cost_id','site','year','quarter','account_name','cost_saved')

class Farming_Solution_CostSavings_Post_Serializer(serializers.ModelSerializer): ####
    class Meta:
        model = PH_Farming_CostSavings
        fields = ('site','year','quarter','account_name','cost_saved','created_dt_pht','last_updated_by')

class Farming_Solution_CostSavings_Put_Serializer(serializers.ModelSerializer): ####
    class Meta:
        model = PH_Farming_CostSavings
        fields = ('site','year','quarter','account_name','cost_saved','updated_dt_pht','last_updated_by')
#---------------------------------------------------------
# class Farming_Solution_Savings_Serializer(serializers.ModelSerializer): ####
#     class Meta:
#         model = PH_Farming_Savings
#         fields = ('cost_id','site_ref','year','quarter','account','amount')

# class Farming_Solution_Savings_POST_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = PH_Farming_Savings
#         fields = ('site_ref','year','quarter','account','amount','created_dt_pht','last_updated_by')

# class Farming_Solution_Savings_PUT_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = PH_Farming_Savings
#         fields = ('site_ref','year','quarter','account','amount','updated_dt_pht','last_updated_by') #

# #--------------------------------------------------------
# class Farming_Solution_Sites_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farming_Solution_Sites
#         fields = ('site_id', 'site_name')

# class Farming_Solution_Savings_CUSTUM_Serializer(serializers.ModelSerializer): #### custom
#     # site_ref = serializers.IntegerField(source='site_ref_id') # no run not nested
#     site_ref =Farming_Solution_Sites_Serializer() # working nested
#     class Meta:
#         model = PH_Farming_Savings
#         fields = ('cost_id','site_ref','year','quarter','account','amount')

# #---

# class Farming_Solution_Sites_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farming_Solution_Sites
#         fields = ('site_id', 'site_name')

# class Farming_Solution_Savings_Accounts_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farming_Solution_Savings_Accounts
#         fields = ('account_id', 'quarter_type','year','account','amount')

# class Farming_Solution_Savings_CUSTUMs_Serializer(serializers.ModelSerializer): #### custom
#     # site_ref = serializers.IntegerField(source='site_ref_id') # to run not nested
#     site_ref = Farming_Solution_Sites_Serializer() # working nested
#     account_ref = Farming_Solution_Savings_Accounts_Serializer(many=True)
#     class Meta:
#         model = PH_Farming_Savings
#         fields = ('cost_id','year','site_ref','account_ref')

# #----
# class Farming_Solution_Savings_Custom_GET_Serializer(serializers.Serializer):
#     site_ref = serializers.IntegerField()
#     site_name = serializers.CharField()
#     year = serializers.IntegerField()
#     quarter = serializers.IntegerField()
#     account = serializers.CharField()
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2)
#     created_dt_pht = serializers.DateTimeField()
#     last_updated_by = serializers.CharField()



# from rest_framework import serializers
# from .models import PH_Farming_Savings, Farming_Solution_Savings_Quarter

# class FarmingSolutionSavingsQuarterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farming_Solution_Savings_Quarter
#         fields = ['quarter_id', 'cost_ref', 'account', 'quarter_type', 'amount']

# class PHFarmingSavingsSerializer(serializers.ModelSerializer):
#     q1_ref = serializers.IntegerField(source='q1_ref_id')
#     # q2_ref = serializers.IntegerField(source='q2_ref_id')
#     # q3_ref = serializers.IntegerField(source='q3_ref_id')
#     # q4_ref = serializers.IntegerField(source='q4_ref_id')
#     class Meta:
#         model = PH_Farming_Savings
#         fields = '__all__'
#         # fields = ['cost_id', 'site_ref', 'year', 'q1_ref', 'q2_ref', 'q3_ref', 'q4_ref']

# class PHFarmingSavingsSerializer(serializers.ModelSerializer):
#     q1 = FarmingSolutionSavingsQuarterSerializer()
#     q2 = FarmingSolutionSavingsQuarterSerializer()
#     q3 = FarmingSolutionSavingsQuarterSerializer()
#     q4 = FarmingSolutionSavingsQuarterSerializer()

#     class Meta:
#         model = PH_Farming_Savings
#         fields = ['cost_id', 'site_ref', 'year', 'q1', 'q2', 'q3', 'q4']

#     def create(self, validated_data):
#         q1_data = validated_data.pop('q1')
#         q2_data = validated_data.pop('q2')
#         q3_data = validated_data.pop('q3')
#         q4_data = validated_data.pop('q4')

#         ph_farming_savings = PH_Farming_Savings.objects.create(**validated_data)

#         Farming_Solution_Savings_Quarter.objects.create(cost_id=ph_farming_savings, **q1_data)
#         Farming_Solution_Savings_Quarter.objects.create(cost_id=ph_farming_savings, **q2_data)
#         Farming_Solution_Savings_Quarter.objects.create(cost_id=ph_farming_savings, **q3_data)
#         Farming_Solution_Savings_Quarter.objects.create(cost_id=ph_farming_savings, **q4_data)

#         return ph_farming_savings





##-------------------------------------------------------

# class FarmingSolutionSavingsQuarterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Farming_Solution_Savings_Quarter
#         fields = ['quarter_id', 'cost_ref', 'account', 'quarter_type', 'amount']

# class PHFarmingSavingsSerializer(serializers.ModelSerializer):
#     q1 = FarmingSolutionSavingsQuarterSerializer(source='q1_savings', required=False)
#     q2 = FarmingSolutionSavingsQuarterSerializer(source='q2_savings', required=False)
#     q3 = FarmingSolutionSavingsQuarterSerializer(source='q3_savings', required=False)
#     q4 = FarmingSolutionSavingsQuarterSerializer(source='q4_savings', required=False)

#     class Meta:
#         model = PH_Farming_Savings
#         fields = ['cost_id', 'site_ref', 'year', 'q1', 'q2', 'q3', 'q4']

#     def create(self, validated_data):
#         q1_data = validated_data.pop('q1_savings', None)
#         q2_data = validated_data.pop('q2_savings', None)
#         q3_data = validated_data.pop('q3_savings', None)
#         q4_data = validated_data.pop('q4_savings', None)

#         instance = PH_Farming_Savings.objects.create(**validated_data)

#         if q1_data:
#             Farming_Solution_Savings_Quarter.objects.create(quarter_type='Q1', **q1_data, ph_farming_savings=instance)
#         if q2_data:
#             Farming_Solution_Savings_Quarter.objects.create(quarter_type='Q2', **q2_data, ph_farming_savings=instance)
#         if q3_data:
#             Farming_Solution_Savings_Quarter.objects.create(quarter_type='Q3', **q3_data, ph_farming_savings=instance)
#         if q4_data:
#             Farming_Solution_Savings_Quarter.objects.create(quarter_type='Q4', **q4_data, ph_farming_savings=instance)

#         return instance