from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Farming_Solution_User,Farming_Solution_Client,Farming_Solution_Type,Farming_Solution_Sites,PH_Farming_Solution
from .serializers import SB_Farming_Project_Serializer,Farming_Solution_User_Serializer, Farming_Solution_Client_Serializer,Farming_Solution_Type_Serializer,Farming_Solution_Sites_Serializer,PH_Farming_Solution_Serializer,PH_Farming_Solution_Custom_Serializer
from datetime import datetime
from django.db import connection, transaction
from .serializers import DateTest_Sites_Serializer, PHF_Action_Logs_Serializer,Post_Sites_Serializer,Post_Client_Serializer, Put_Client_Serializer, Freeze_Client_Serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.db import connections
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["POST"])
def create_project(request):
    data = request.data
    data['created_dt_pht'] = datetime.now()
    inserted_by = data['last_updated_by']
    serializer = SB_Farming_Project_Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        instance = serializer.save()
        instance_id = instance.farming_ident
        log_data = {
        'id_ref' : instance_id,
        'page' : 'SubmitForm project',
        'action' : 'create',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
       
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def list_sites(request):
    sites = Farming_Solution_Sites.objects.all()
    serializer = Farming_Solution_Sites_Serializer(sites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_site(request):
    site = Farming_Solution_Sites.objects.all()
    serializer = Farming_Solution_Sites_Serializer(site, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def create_site(request):
    data = request.data
    data['created_dt_pht'] = datetime.now()
    inserted_by = data['last_updated_by']
    serializer = Post_Sites_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.save()
        instance_id = instance.site_id
        log_data = {
        'id_ref' : instance_id,
        'page' : 'SubmitForm site',
        'action' : 'create',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def list_types(request):
    users = Farming_Solution_Type.objects.all()
    serializer = Farming_Solution_Type_Serializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_clients(request):
    clients = Farming_Solution_Client.objects.all()
    serializer = Farming_Solution_Client_Serializer(clients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_client(request, id):
    client = Farming_Solution_Client.objects.get(client_id=id)
    serializer = Farming_Solution_Client_Serializer(client, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def create_client(request):
    data = request.data
    data['created_dt_pht'] = datetime.now()
    inserted_by = data['last_updated_by']
    serializer = Post_Client_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        instance = serializer.save()
        instance_id = instance.client_id
        log_data = {
        'id_ref' : instance_id,
        'page' : 'SubmitForm client',
        'action' : 'create',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def client_update(request, id):
    data = request.data
    inserted_by = data['last_updated_by']
    data['updated_dt_pht'] = datetime.now()
    try:
        client = Farming_Solution_Client.objects.get(client_id=id)
    except Farming_Solution_Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    log_data = {
        'id_ref' : client.client_id,
        'page' : 'client',
        'action' : 'update',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
    
    serializer = Put_Client_Serializer(instance=client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def freeze_client(request, id):
    data = request.data
    inserted_by = data['last_updated_by']
    log_data = {
        'id_ref' : id,
        'page' : 'Client',
        'action' : 'freeze',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(),
    }
    client = Farming_Solution_Client.objects.get(client_id=id)
    if client.is_active == 1:
        client.is_active = 0
    elif client.is_active == 0:
        client.is_active = 1
    client.updated_dt_utc = datetime.now()
    serializer = Freeze_Client_Serializer(client, data=request.data)
    if serializer.is_valid():
        client.save()
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_users(request):
    users = Farming_Solution_User.objects.all()
    serializer = Farming_Solution_User_Serializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_user(request,id):
    user = Farming_Solution_User.objects.get(user_id=id)
    serializer = Farming_Solution_User_Serializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
