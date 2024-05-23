from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, CcmsSerializer, UpdateUserSerializer, FreezeUserSerializer, DeleteUserSerializer, UpdateUserRoleSerializer, CustomUserSerializer
from django.db import connections
from django.contrib.sessions.models import Session

from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_users(request):
    if request.method == 'GET':
        user = User.objects.all().order_by('-employee_full_name')
        user_Serializer = UserSerializer(instance=user, many=True)
        return Response(user_Serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        login_id = request.data.get('login_id')
    
        try:
            user = User.objects.get(login_id=login_id)    
            if user.status == 'active':
                return Response({'message': 'Access has already been approved. No further action is needed.'}, status=status.HTTP_409_CONFLICT)
            elif user.status == 'pending':
                return Response({'message': 'Your request has been received and is awaiting approval.'}, status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            try:
                request.data['status'] = 'active'
                user = User.objects.create_user(**request.data)
                return Response({'message': 'User created successfully'})
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        except :
            return Response({'message': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)

# @csrf_exempt  
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_user(request):
    login_id = request.data.get('login_id')
    try:
        user = User.objects.get(login_id=login_id)    
        if user.status == 'active':
            return Response({'message': 'Access has already been approved. No further action is needed.'}, status=status.HTTP_409_CONFLICT)
        elif user.status == 'pending':
            return Response({'message': 'Your request has been received and is awaiting approval.'}, status=status.HTTP_409_CONFLICT)
    except User.DoesNotExist:
        try:
            request.data['status'] = 'active'
            user = User.objects.create_user(**request.data)
            return Response({'message': 'User created successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    except :
        return Response({'message': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT']) 
def update_user(request):
    login_id = request.data.get('login_id')
    user_role = request.data.get('user_role')
    try:
        user = User.objects.get(login_id=login_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.user_role = user_role
    serializer = UpdateUserRoleSerializer(user, data=request.data)
    if serializer.is_valid():
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) 
def freeze_user(request,pk):
    login_id = request.data.get('login_id')
    try:
        user = User.objects.get(login_id=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user.status == "active":
        user.status = "inactive"
    elif user.status == "inactive":
        user.status = "active"
    
    serializer = FreezeUserSerializer(user, data=request.data)
    if serializer.is_valid():
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT']) 
def delete_user(request):
    login_id = request.data.get('login_id')
    try:
        user = User.objects.get(login_id=login_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user.is_active == 1:
        user.is_active = 0
    elif user.is_active == 0:
        user.is_active = 1
    
    serializer = DeleteUserSerializer(user, data=request.data)
    if serializer.is_valid():
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_employee(request:Request):
    query = request.query_params.get('query')
    if query.isdigit(): 
        sql_query = """
            SELECT TOP 3 employee_ident, employee_common_name, login_id, email1 FROM CCMS_Employee WHERE [employee_ident] LIKE CONCAT('%%', %s, '%%') 
            and status = 'active'
        """
        # 
    else:
        sql_query = """
            SELECT TOP 3 employee_ident, employee_common_name, login_id, email1 FROM CCMS_Employee WHERE [employee_common_name] LIKE CONCAT('%%', %s, '%%')
            and status = 'active'  
        """
        # 
    
    with connections['ccms_db'].cursor() as cursor:
        cursor.execute(sql_query, [query])
        results = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    if results:  
        serializer = CcmsSerializer(data=results, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("No results found", status=status.HTTP_404_NOT_FOUND)

# @csrf_exempt        
@api_view(['POST'])
def login_request(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
 
        if user is not None:
            login(request, user)
            # token, created = Token.objects.get_or_create(user=user)
            user_Serializer = CustomUserSerializer(user)
            return Response({'user': user_Serializer.data})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
           
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
def logout_request(request):
    logout(request)
    return JsonResponse({'message': 'Successfully logged out'})

@csrf_exempt  
@api_view(['GET'])
def rehydrate_user_info(request):
    session_id = request.COOKIES.get('sessionid')

    if session_id:
        session_data = Session.objects.get(session_key=session_id).get_decoded()
        user_id = session_data.get('_auth_user_id')

        if user_id:
            user = User.objects.get(pk=user_id)
            user_Serializer = CustomUserSerializer(user)
            return Response({'user': user_Serializer.data})
        else:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'Session ID not found'}, status=400)