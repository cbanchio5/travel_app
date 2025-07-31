"""
URL configuration for travel_app_backend project.

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
from django.urls import path
from apps.users import views
from apps.users.views import CustomAuthToken
from apps.users.views import UserCreateView
from apps.itinerary.views import TestItineraryGeneratorView
from apps.itinerary.views import ItineraryTaskStatusView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.index),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('test-generator/', TestItineraryGeneratorView.as_view(), name='test-itinerary'),
    path('itinerary-status/<uuid:task_id>/', ItineraryTaskStatusView.as_view(), name='itinerary-status')
]



