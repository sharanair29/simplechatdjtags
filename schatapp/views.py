from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from simple_chatbot.views import SimpleChatbot
# Create your views here.

def index(request):
    return render(request, 'trialbot/bot.html')


from django.test.client import RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
import json
from django.http import JsonResponse
client = APIClient()
factory = APIRequestFactory()
import simplejson as JSON

from django.test import Client
c = Client()

@csrf_exempt
def get(request):
    userText = str(request.GET.get("msg")) # data from input
    # data = {"message" : {userText}}
    data = {"message" : f'{userText}'}
    print(data)

    while True:
        # reply = SimpleChatbot.as_view()
        url = 'http://localhost:8000/simple_chatbot/'
        
        ask = c.post(url, data=data, content_type='application/json')
        # ask2 = c.get(url, data=data, content_type='application/json')
        # print(ask)
        # bot_reply = reply(ask)
        # bot_reply = "Hope it works"
        # print(bot_reply)
        # return HttpResponse(str(12345))
        value = ask
        return HttpResponse(value)


