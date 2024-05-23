"""
URL configuration for PHFarming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf_token_endpoint(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

urlpatterns = [ #ph-farming-solution/
    path(
        "api/",
        include(
            [
                path('admin/', admin.site.urls),
                path('dashboard/', include("Dashboard.urls")),
                path('tracker/', include("Tracker.urls")),
                path('rfp/', include("RFP.urls")),
                path('submitform/', include("SubmitForm.urls")),
                path('user/', include("User.urls")),
                path('workload/', include("workload.urls")),
                path('costsavings/', include("costsavings.urls")),
                path('csrf/', csrf_token_endpoint, name='get_csrf_token'),
            ]
        )
    )
]
