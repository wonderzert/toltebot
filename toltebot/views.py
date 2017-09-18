# -*- coding: utf-8 -*-
from django.shortcuts import render
from . import tgbot
from .tgbot import *

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def toltebot(request):
    # print(request.body)
    ans = tgbot.handle_update(request.body)
    if (ans):
        return HttpResponse(ans)
    return HttpResponse("Hello, world?")
