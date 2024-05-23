from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import connection, transaction
from rest_framework import status
import logging
from django.db.models import F
from .models import PH_Farming_CostSavings #, Farming_Solution_Savings_Quarter
from .serializers import Farming_Solution_CostSavings_Serializer,Farming_Solution_CostSavings_Post_Serializer,Farming_Solution_CostSavings_Put_Serializer #, Farming_Solution_Savings_Serializer, Farming_Solution_Savings_POST_Serializer, Farming_Solution_Savings_PUT_Serializer, Farming_Solution_Savings_Custom_GET_Serializer, Farming_Solution_Sites_Serializer, Farming_Solution_Savings_CUSTUM_Serializer ,Farming_Solution_Savings_CUSTUMs_Serializer
from SubmitForm.serializers import PHF_Action_Logs_Serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.db import connections
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt



# from .serializers import PHFarmingSavingsSerializer

# @api_view(["GET"]) #ori no nested
# def costsavings(request):
#     costsavings = PH_Farming_Savings.objects.all()
#     serializer = Farming_Solution_Savings_Serializer(instance=costsavings, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["GET"]) #working nested sites
# def costsavings(request):
#     costsavings = PH_Farming_Savings.objects.all()
#     serializer = Farming_Solution_Savings_CUSTUM_Serializer(instance=costsavings, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"]) # 
def costsavings(request):
    costsavings = PH_Farming_CostSavings.objects.all()
    serializer = Farming_Solution_CostSavings_Serializer(instance=costsavings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    # custom
    # costsavings = PH_Farming_Savings.objects.all()
    # serializer = Farming_Solution_Savings_CUSTUMs_Serializer(instance=costsavings, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    
    #------------------------------------------
    # costsavings = PH_Farming_Savings.objects.all()
    # #Join operation to get site_name instead of site_ref
    # # Assuming 'site_ref' in PH_Farming_Savings maps to 'site_id' in Farming_Solution_Sites
    # costsavings_with_site_name = costsavings.annotate(site_name=F('site_ref__site_ref'))
    
    # serializer = Farming_Solution_Savings_Custom_GET_Serializer(instance=costsavings_with_site_name, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)
# get request data and create value for missing fields
@api_view(["POST"])
def costsavings_create(request):
    data = request.data
    data['created_dt_pht'] = datetime.now()
    inserted_by = data['last_updated_by']
    serializer = Farming_Solution_CostSavings_Post_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.save()
        instance_id = instance.cost_id
        log_data = {
        'id_ref' : instance_id,
        'page' : 'CostSavings',
        'action' : 'create',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def costsavings_update(request, id):
    data = request.data
    data['updated_dt_pht'] = datetime.now()
    try:
        costsavings = PH_Farming_CostSavings.objects.get(cost_id=id)
    except PH_Farming_CostSavings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    log_data = {
        'id_ref' : costsavings.cost_id,
        'page' : 'CostSavings',
        'action' : 'update',
        'inserted_by' : costsavings.last_updated_by,
        'inserted_date_time_ph': datetime.now(), }
    serializer = Farming_Solution_CostSavings_Put_Serializer(instance=costsavings, data=request.data)
    if serializer.is_valid():
        serializer.save()
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def costsavings_delete(request,id):
    data = request.data
    inserted_by = data['last_updated_by']
    try:
        instance = PH_Farming_CostSavings.objects.get(cost_id=id)
    except PH_Farming_CostSavings.DoesNotExist:
        return Response({"error": f"PH Farming Savings data does not exist"}, status=status.HTTP_404_NOT_FOUND)
    log_data = {
        'id_ref' : id,
        'page' : 'CostSavings',
        'action' : 'delete',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
    action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
    if action_logs_serializer.is_valid():
        action_logs_serializer.save()
    instance.delete()
    return Response({"success": f"PH Farming Savings data successfully deleted"}, status=status.HTTP_200_OK)
    # return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def ph_farming_savings(request):
#     if request.method == 'GET':
#         ph_farming_savings = PH_Farming_Savings.objects.all()
#         serializer = Farming_Solution_Savings_Serializer(ph_farming_savings, many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def ph_farming_savings(request):
#     if request.method == 'GET':
#         ph_farming_savings = PH_Farming_Savings.objects.all()
#         serializer = PHFarmingSavingsSerializer(ph_farming_savings, many=True)
#         return Response(serializer.data)

#---------------------------------

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import PHFarmingSavingsSerializer
# from .models import PH_Farming_Savings

# @api_view(['GET'])
# def ph_farming_savings_api(request):
#     if request.method == 'GET':
#         ph_farming_savings = PH_Farming_Savings.objects.all()
#         serializer = PHFarmingSavingsSerializer(ph_farming_savings, many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def farming_savings_quarters(request):
#     if request.method == 'GET':
#         quarters = Farming_Solution_Savings_Quarter.objects.all()
#         # Serialize the data if needed before returning the response
#         serialized_quarters = serialize_quarters(quarters)  # Implement this serialization function
#         return Response(serialized_quarters)
# def serialize_quarters(quarters):
#     # Implement your serialization logic here
#     serialized_data = [{'quarter_id': quarter.quarter_id, 'cost_ref': quarter.cost_ref, 'account': quarter.account,
#                         'quarter_type': quarter.quarter_type, 'amount': quarter.amount} for quarter in quarters]
#     return serialized_data




#   select 
#   cs.cost_id,cs.site_ref,cs.year,
#   qs1.quarter_id as Q1_quarter_id,  qs1.account as Q1_account, qs1.amount as Q1_amount,
#   qs2.quarter_id as Q2_quarter_id,  qs2.account as Q2_account, qs2.amount as Q2_amount,
#   qs3.quarter_id as Q3_quarter_id,  qs3.account as Q3_account, qs3.amount as Q3_amount,
#   qs4.quarter_id as Q4_quarter_id,  qs4.account as Q4_account, qs4.amount as Q4_amount
  
#   from farming_solution_savingss as cs
#   inner join
#   farming_solution_quarter_savingss as qs1 
#   on qs1.quarter_id = cs.q1_ref_id

#   inner join
#   farming_solution_quarter_savingss as qs2 
#   on qs2.quarter_id = cs.q2_ref_id
 
#    inner join
#   farming_solution_quarter_savingss as qs3 
#   on qs3.quarter_id = cs.q3_ref_id

#     inner join
#   farming_solution_quarter_savingss as qs4 
#   on qs4.quarter_id = cs.q4_ref_id