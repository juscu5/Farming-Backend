from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import connection, transaction
from rest_framework import status
import logging
from SubmitForm.models import PH_Farming_Solution, Farming_Solution_User
from SubmitForm.serializers import PHF_Action_Logs_Serializer, Farming_Solution_User_Serializer
from .serializers import Workload_Farming_Solution_Custom_Serializer, Workload_Farming_Solution_Serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.db import connections
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
import json

@api_view(["GET"])
def workload(request):
    tracker = PH_Farming_Solution.objects.filter(status='In progress', is_active=True)
    
    serializer =  Workload_Farming_Solution_Serializer(instance=tracker, many=True)
    # serializer = Workload_Farming_Solution_Custom_Serializer(instance=tracker, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_comments(request, id):
    try:
        workload = PH_Farming_Solution.objects.get(farming_ident=id)
    except PH_Farming_Solution.DoesNotExist:
        return Response({"Message": "Workload not found"}, status=status.HTTP_404_NOT_FOUND)
    
    data = json.loads(request.body)
    comments_progress = data.get('comments_progress')

    workload.comments_progress = comments_progress 
    workload.save()

    # Retrieve user details
    user_ref = workload.user_ref
    try:
        user = Farming_Solution_User.objects.get(user_id=user_ref.user_id)
    except Farming_Solution_User.DoesNotExist:
        return Response({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Construct user's full name
    user_fullname = f"{user.first_name} {user.last_name}"

    # Create log data
    log_data = {
        'id_ref': id,
        'page': 'cost savings',
        'action': 'update',
        'inserted_by': user_fullname,
        'inserted_date_time_ph': datetime.now(),
    }

    # Save action logs
    action_logs_serializer = PHF_Action_Logs_Serializer(data=log_data)
    if action_logs_serializer.is_valid():
        action_logs_serializer.save()
    return Response({"Message": comments_progress}, status=status.HTTP_200_OK)
    # return Response({"Message": user_fullname}, status=status.HTTP_200_OK)