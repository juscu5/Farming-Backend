from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from SubmitForm.models import PH_Farming_Solution, Farming_Solution_User
from .serializers import RFP_PH_Farming_Get_Serializer,RFP_Farming_Solution_Put_Custom_Serializer,RFP_Farming_Solution_delete_Custom_Serializer
from SubmitForm.serializers import PHF_Action_Logs_Serializer

@api_view(["GET"])
def rfp_project_list(request):
    rfp = PH_Farming_Solution.objects.filter(status='RFP',is_active=True)
    serializer = RFP_PH_Farming_Get_Serializer(rfp, many=True)
    return Response(serializer.data)

#get rfp, get user_first_name+last_name using rfp.user_ref
@api_view(['PUT'])
def rfp_update(request, id):
    data = request.data
    inserted_by = data['last_updated_by']
    data['updated_dt_utc'] = timezone.now()
    try:
        rfp = PH_Farming_Solution.objects.get(farming_ident=id)
    except PH_Farming_Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RFP_Farming_Solution_Put_Custom_Serializer(rfp, data=request.data)
    if serializer.is_valid():
        serializer.save()

        log_data = { 'id_ref' : id,
        'page' : 'RFP',
        'action' : 'update',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }

        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) 
def rfp_remove(request, id):
    # inserted_by = request.query_params.get('inserted_by')
    data = request.data
    inserted_by = data['last_updated_by']
    try:
        rfp = PH_Farming_Solution.objects.get(farming_ident=id)
    except PH_Farming_Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if rfp.is_active == 1:
        rfp.is_active = 0
    elif rfp.is_active == 0:
        rfp.is_active = 1
    
    rfp.updated_dt_utc = timezone.now()
    serializer = RFP_Farming_Solution_delete_Custom_Serializer(rfp, data=request.data)
    if serializer.is_valid():
        rfp.save()
        log_data = { 'id_ref' : id,
        'page' : 'RFP',
        'action' : 'freeze',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

