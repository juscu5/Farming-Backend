from django.contrib.auth.backends import ModelBackend
from .serializers import AuthLogSerializer
from datetime import datetime
from .models import User
# import requests #uncomment in dev/prod
import logging
import base64

logger = logging.getLogger(__name__)

def authLogin(username, password):
    # base_url = 'https://www.wblt.ccms.teleperformance.com/authentication'
    # auth = "Basic " + base64.b64encode(bytes(f"{username}:{password}", 'utf-8')).decode('utf-8')
    # headers = {'Authorization': auth}
    
    # try:
    #     resp = requests.get(base_url, headers=headers)
    #     if resp.status_code == 200:
    #         return True
    #     else:
    #         return False
    # except Exception as e:
    #     return False
    return True

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(login_id=username, status='active')
        except User.DoesNotExist:
            return None
        
        log_data = {
            'login_id': username,
            'inserted_date_time_ph': datetime.now(),
        }
        
        if authLogin(username, password):
            # logger.info(f'Login User: {username}') 
            auth_logs_serializer = AuthLogSerializer(data=log_data)
            if auth_logs_serializer.is_valid():
                auth_logs_serializer.save()
            return user
        # logger.error(f'Failed Login: {username}')
