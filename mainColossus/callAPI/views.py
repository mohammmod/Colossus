from django.shortcuts import render
import requests
from django.http import HttpResponse
import json


def getWelcome(request):
    return HttpResponse("hello there")


def getApiData(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type="application/json")