from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import callAPI


urlpatterns = [

    path('getAPI', views.getWelcome, name="getWelcome"),
    path('', callAPI.as_view(template_name='callAPI.html'), name='callAPI'),
]

