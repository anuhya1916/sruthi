from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Event_Head


# Create your views here.
def home(request):
    return render(request,'home.html',None)