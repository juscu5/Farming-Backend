from django.db import models

# Create your models here.

class Farming_Solution_User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    ccms_id = models.IntegerField(null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    middle_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    ccms_uname = models.CharField(max_length=50, null=False, blank=False)
    user_type = models.CharField(max_length=50, null=False, blank=False)
    created_dt_utc = models.DateTimeField(null=False, blank=False)
    updated_dt_utc = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'farming_solution_user'
    # def __str__(self):
    #     return self.last_name   

    
class Farming_Solution_Client(models.Model):
    client_id = models.AutoField(primary_key=True, editable=False)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    project_name = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=50, null=True, blank=True)
    created_dt_utc = models.DateTimeField(null=False, blank=False)
    updated_dt_utc = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'farming_solution_client'
    # def __str__(self):
    #     return self.project_name   
  
class Farming_Solution_Type(models.Model):
    type_id = models.AutoField(primary_key=True, editable=False)
    type_name = models.CharField(max_length=50, null=True, blank=True)
    created_dt_utc = models.DateTimeField(null=False, blank=False)
    updated_dt_utc = models.DateTimeField(null=True, blank=True) 
    last_updated_by = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    
    class Meta:
        db_table = 'farming_solution_type'
    # def __str__(self):
    #     return self.type_name

    
class Farming_Solution_Sites(models.Model):
    site_id = models.AutoField(primary_key=True, editable=False)
    site_name = models.CharField(max_length=50, null=True, blank=True)
    created_dt_utc = models.DateTimeField(null=False, blank=False)
    updated_dt_utc = models.DateTimeField(null=True, blank=True) 
    last_updated_by = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'farming_solution_sites'
    # def __str__(self):
    #     return self.site_name


class PH_Farming_Solution(models.Model):
    farming_ident = models.AutoField(primary_key=True, editable=False)
    type_ref = models.ForeignKey(Farming_Solution_Type, on_delete=models.DO_NOTHING, null=False, editable=True)
    sites_ref = models.ForeignKey(Farming_Solution_Sites, on_delete=models.DO_NOTHING, null=False, editable=True)
    client_ref = models.ForeignKey(Farming_Solution_Client, on_delete=models.DO_NOTHING, null=False, editable=True)
    user_ref = models.ForeignKey(Farming_Solution_User, on_delete=models.DO_NOTHING, null=False, editable=True)

    seat_req = models.CharField(max_length=50, null=True, blank=True) 
    need = models.CharField(max_length=50, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    requested_date = models.DateTimeField( null=False) #auto_now_add=True,
    target_date = models.CharField(max_length=50, null=True, blank=True)
    resolved_date = models.DateTimeField(null=True, blank=True) 
    resolved_days = models.CharField(max_length=50, null=True, blank=True)
    critical_item = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    solution = models.CharField(max_length=255, null=True, blank=True)
    email_trail = models.CharField(max_length=255, null=True, blank=False)
    requestor = models.CharField(max_length=50, null=True, blank=True)
    comments_progress = models.CharField(max_length=255, null=True, blank=True)
    created_dt_utc = models.DateTimeField(null=False, blank=False) 
    updated_dt_utc = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    
    class Meta:
        db_table = 'farming_solution_projects'
    # def __str__(self):
    #     return self.farming_ident
        
class PH_Farming_Action_Logs(models.Model):
    log_id = models.AutoField(primary_key=True, editable=False)
    id_ref = models.IntegerField(null=True)
    action = models.CharField(max_length=30, null=True)
    page = models.CharField(max_length=30, null=True)
    inserted_by = models.CharField(max_length=30, null=True)
    inserted_date_time_ph = models.DateTimeField(null=True)
    class Meta:
        db_table = 'phf_action_logs'