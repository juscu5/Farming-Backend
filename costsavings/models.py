from django.db import models
from SubmitForm.models import Farming_Solution_Sites

# as is
class PH_Farming_CostSavings(models.Model): 
    cost_id = models.AutoField(primary_key=True, editable=False) #1
    site = models.CharField(max_length=30, null=True) #Aura
    year = models.IntegerField(null=True) #2023
    quarter = models.CharField(max_length=2, null=True, blank=True) # Q1, Q2, Q3, Q4
    account_name = models.CharField(max_length=30, null=True) #Tiktok
    cost_saved = models.IntegerField(null=True) #100,000
    created_dt_pht = models.DateTimeField(null=False, blank=False) 
    updated_dt_pht = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=30, null=True)
    class Meta:
        db_table = 'farming_solution_costsavings'


# class Farming_Solution_Savings_Accounts(models.Model):
#     account_id = models.AutoField(primary_key=True, editable=False)
#     quarter_type = models.CharField(max_length=2, null=True, blank=True) # Q1, Q2, Q3, Q4
#     year = models.IntegerField(null=True)
#     account = models.CharField(max_length=50, null=True)
#     amount = models.IntegerField(null=True) 
#     class Meta:
#         db_table = 'farming_solution_accounts'

#working nested site_ref, account_ref(many=true) sampledb25
# class PH_Farming_Savings(models.Model): 
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     year = models.IntegerField(null=True)
#     site_ref = models.ForeignKey(Farming_Solution_Sites, on_delete=models.DO_NOTHING, null=False, editable=True)
#     account_ref = models.ForeignKey(Farming_Solution_Savings_Accounts, on_delete=models.DO_NOTHING,  editable=True)
#     created_dt_pht = models.DateTimeField(null=False, blank=False)
#     updated_dt_pht = models.DateTimeField(null=True, blank=True)
#     last_updated_by = models.CharField(max_length=30, null=True)
#     class Meta:
#         db_table = 'farming_solution_savingss'

# #working nested site_ref, account_ref sampledb24
# class PH_Farming_Savings(models.Model): 
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     year = models.IntegerField(null=True)
#     site_ref = models.ForeignKey(Farming_Solution_Sites, on_delete=models.DO_NOTHING, null=False, editable=True)
#     account_ref = models.ForeignKey(Farming_Solution_Savings_Accounts, on_delete=models.DO_NOTHING, null=False, editable=True)
#     created_dt_pht = models.DateTimeField(null=False, blank=False)
#     updated_dt_pht = models.DateTimeField(null=True, blank=True)
#     last_updated_by = models.CharField(max_length=30, null=True)
#     class Meta:
#         db_table = 'farming_solution_savingss'

#working nested site_ref sampledb23
# class PH_Farming_Savings(models.Model): 
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     site_ref = models.ForeignKey(Farming_Solution_Sites, on_delete=models.DO_NOTHING, null=False, editable=True)
#     year = models.IntegerField(null=True)
#     quarter = models.CharField(max_length=2, null=True, blank=True) # Q1, Q2, Q3, Q4
#     account = models.CharField(max_length=50, null=True)
#     amount = models.IntegerField(null=True) 
#     created_dt_pht = models.DateTimeField(null=False, blank=False)
#     updated_dt_pht = models.DateTimeField(null=True, blank=True)
#     last_updated_by = models.CharField(max_length=30, null=True)
#     class Meta:
#         db_table = 'farming_solution_savingss'

# original
# class PH_Farming_Savings(models.Model):
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     site_ref = models.IntegerField(null=True)
#     year = models.IntegerField(null=True)
#     quarter = models.CharField(max_length=2, null=True, blank=True) # Q1, Q2, Q3, Q4
#     account = models.CharField(max_length=50, null=True)
#     amount = models.IntegerField(null=True) 
#     created_dt_pht = models.DateTimeField(null=False, blank=False)
#     updated_dt_pht = models.DateTimeField(null=True, blank=True)
#     last_updated_by = models.CharField(max_length=30, null=True)
#     class Meta:
#         db_table = 'farming_solution_savings'



# class Farming_Solution_Savings_Quarter(models.Model):
#     quarter_id = models.AutoField(primary_key=True, editable=False)
#     cost_ref = models.IntegerField(null=True)
#     account = models.CharField(max_length=50, null=True)
#     quarter_type = models.CharField(max_length=2, null=True, blank=True) # Q1, Q2, Q3, Q4
#     amount = models.IntegerField(null=True) 
    
#     class Meta:
#         db_table = 'farming_solution_quarter_savingss'

# class PH_Farming_Savings(models.Model):
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     site_ref = models.IntegerField(null=True)
#     year = models.IntegerField(null=True)

#     q1_ref = models.ForeignKey(Farming_Solution_Savings_Quarter, on_delete=models.DO_NOTHING, null=True)
#     # q2_ref = models.ForeignKey(Farming_Solution_Savings_Quarter, on_delete=models.DO_NOTHING, related_name='q2_savings', null=True)
#     # q3_ref = models.ForeignKey(Farming_Solution_Savings_Quarter, on_delete=models.DO_NOTHING, related_name='q3_savings', null=True)
#     # q4_ref = models.ForeignKey(Farming_Solution_Savings_Quarter, on_delete=models.DO_NOTHING, related_name='q4_savings', null=True)
   
#     class Meta:
#         db_table = 'farming_solution_savingss'

     # q1_ref = models.OneToOneField(Farming_Solution_Savings_Quarter, related_name='q1', null=True, blank=True, on_delete=models.CASCADE)
    # q2_ref = models.OneToOneField(Farming_Solution_Savings_Quarter, related_name='q2', null=True, blank=True, on_delete=models.CASCADE)
    # q3_ref = models.OneToOneField(Farming_Solution_Savings_Quarter, related_name='q3', null=True, blank=True, on_delete=models.CASCADE)
    # q4_ref = models.OneToOneField(Farming_Solution_Savings_Quarter, related_name='q4', null=True, blank=True, on_delete=models.CASCADE)

    # created_dt_pht = models.DateTimeField(null=True)
    # updated_dt_pht = models.DateTimeField(null=True)
    # last_updated_by = models.CharField(max_length=30, null=True)
    
    
#---- ori

# class Farming_Solution_Savings_Quarter(models.Model):
#     quarter_id = models.AutoField(primary_key=True, editable=False)
#     cost_ref = models.CharField(max_length=50, null=True, blank=True)
#     account = models.CharField(max_length=50, null=True)
#     amount = models.IntegerField( null=True) #max_digits=10, decimal_places=2
#     created_dt_utc = models.DateTimeField(null=False, blank=False)
#     updated_dt_utc = models.DateTimeField(null=True, blank=True)
#     is_active = models.BooleanField(null=False, blank=False, default=True)

#     class Meta:
#         db_table = 'farming_solution_quarter_savings'


# class PH_Farming_Savings(models.Model):
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     site_ref = models.IntegerField(null=True)
#     year = models.IntegerField(null=True)
#     quarter = models.ForeignKey(Farming_Solution_Savings_Quarter, on_delete=models.DO_NOTHING, null=False, editable=True)
# #     account = models.CharField(max_length=50, null=True)
# #     amount = models.IntegerField( null=True) #max_digits=10, decimal_places=2
#     created_dt_pht = models.DateTimeField(null=True)
#     updated_dt_pht = models.DateTimeField(null=True)
#     last_updated_by = models.CharField(max_length=30, null=True)
#     class Meta:
#         db_table = 'farming_solution_savings'

#--------------------------------------------------------------------------
# class Farming_Solution_Savings_Quarter(models.Model):
#     quarter_id = models.AutoField(primary_key=True, editable=False)
#     cost_ref = models.CharField(max_length=50, null=True, blank=True)
#     account = models.CharField(max_length=50, null=True)
#     quarter_type = models.CharField(max_length=2, null=True, blank=True) #Q1, Q2, Q3, Q4
#     amount = models.IntegerField( null=True) 
#     class Meta:
#         db_table = 'farming_solution_quarter_savings'

# class PH_Farming_Savings(models.Model):
#     cost_id = models.AutoField(primary_key=True, editable=False)
#     site_ref = models.IntegerField(null=True)
#     year = models.IntegerField(null=True)
#     # q1 = models.ForeignKey(Farming_Solution_Savings_Quarter, related_name='Q1', on_delete=models.CASCADE)
#     # q2 = models.ForeignKey(Farming_Solution_Savings_Quarter, related_name='Q2', on_delete=models.CASCADE)
#     # q3 = models.ForeignKey(Farming_Solution_Savings_Quarter, related_name='Q3', on_delete=models.CASCADE)
#     # q4 = models.ForeignKey(Farming_Solution_Savings_Quarter, related_name='Q4', on_delete=models.CASCADE)

#     # created_dt_pht = models.DateTimeField(null=True)
#     # updated_dt_pht = models.DateTimeField(null=True)
#     # last_updated_by = models.CharField(max_length=30, null=True)

#     class Meta:
#         db_table = 'farming_solution_savings'