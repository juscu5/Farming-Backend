from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import connection, transaction
from rest_framework import status
import logging
from SubmitForm.models import PH_Farming_Solution
from .serializers import Tracker_Farming_Solution_Serializer, Tracker_Farming_Solution_Put_Custom_Serializer ,Tracker_Farming_Solution_delete_Custom_Serializer,PHF_Action_Logs_Serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.db import connections
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@api_view(["GET"])
def tracker_projects(request):
    tracker = PH_Farming_Solution.objects.exclude(status='RFP').filter(is_active=True)
    serializer = Tracker_Farming_Solution_Serializer(instance=tracker, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def tracker_update(request, id):
    data = request.data
    data['updated_dt_utc'] = datetime.now()
    inserted_by = data['last_updated_by']
    try:
        tracker = PH_Farming_Solution.objects.get(farming_ident=id)
    except PH_Farming_Solution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    log_data = {
        'id_ref' : tracker.farming_ident,
        'page' : 'Tracker',
        'action' : 'update',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(), }
    tracker.updated_dt_utc = datetime.now()
    serializer = Tracker_Farming_Solution_Put_Custom_Serializer(tracker, data=request.data)
    if serializer.is_valid():
        serializer.save()
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_freeze(request, id):
    # inserted_by = request.query_params.get('inserted_by')
    data = request.data
    inserted_by = data['last_updated_by']
    log_data = {
        'id_ref' : id,
        'page' : 'Tracker',
        'action' : 'freeze',
        'inserted_by' : inserted_by,
        'inserted_date_time_ph': datetime.now(),
    }
    tracker = PH_Farming_Solution.objects.get(farming_ident=id)
    if tracker.is_active == 1:
        tracker.is_active = 0
    elif tracker.is_active == 0:
        tracker.is_active = 1
    tracker.updated_dt_utc = datetime.now()
    serializer = Tracker_Farming_Solution_delete_Custom_Serializer(tracker, data=request.data)
    if serializer.is_valid():
        tracker.save()
        action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
        if action_logs_serializer.is_valid():
            action_logs_serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
