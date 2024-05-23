from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Farming_Solution_User)
admin.site.register(Farming_Solution_Client)
admin.site.register(Farming_Solution_Type)
admin.site.register(Farming_Solution_Sites)
admin.site.register(PH_Farming_Solution)