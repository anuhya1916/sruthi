from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Event_Head
from user.models import Event


# Create your views here.
def home(request):
        events_list=requests.get("https://shruthiapi.herokuapp.com/events")
        return render(request,'home.html',{'events_list': events_list.json()})
   