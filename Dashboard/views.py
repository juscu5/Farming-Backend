from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from SubmitForm.models import PH_Farming_Solution
from .serializers import Dashboard_Serializer
from SubmitForm.serializers import PH_Farming_Solution_Serializer
from django.db.models import Count

@api_view(["GET"])
def list_all_serializer(request):
    dashboard = PH_Farming_Solution.objects.all()
    serializer = PH_Farming_Solution_Serializer(dashboard, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(["GET"])
def list_dashboard(request):
    dashboard = PH_Farming_Solution.objects.all()
    serializer = Dashboard_Serializer(dashboard, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
