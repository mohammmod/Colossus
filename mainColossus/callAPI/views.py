from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from django.views.generic import TemplateView
from . import services

def getWelcome(request):
    response = services.callAPI()
    return HttpResponse(response)

def showInfo(request, name):
    info = services.getdatePage(name)

    return HttpResponse(json.dumps(info), content_type="application/json")


def getApiData(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


class callAPI(TemplateView):
    template_name = 'callAPI.html'
    def get_context_data(self, *args, **kwargs):
        pass
