from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [

    path('getApi', views.getApiData, name="getApiData"),
    path('', views.getWelcome, name="getWelcome")
]

