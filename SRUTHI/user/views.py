from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def user_login(request):
    message=User.objects.order_by('Rollno')
    context={'message':message}
    return render(request,'user_login.html',context)
def user_registration(request):
    return render(request,'user_registration.html',None)
def registration(request):
    if request.method=="POST":
        #obj=User()
        name=request.POST['name']
        password=request.POST['pw']
        college=request.POST['clname']
        Rollno=request.POST['rno']
        branch=request.POST['branch']
        year=request.POST['year']
        mobile_no=request.POST['mobile no']
        email_id=request.POST['email']
        data={'password':password,'name':name,'Rollno':Rollno,'college':college,'branch':branch,'year':year, 'mobile_no':mobile_no,'email_id':email_id}
        r=requests.post('https://shruthiapi.herokuapp.com/user_register',data)
        k=request.POST.get('name')+"  is registered"
        messages.success(request,k)
        return render(request,'user_login.html',None)
def api_call(request):
    Rollno=request.POST.get('Rollno')
    password=request.POST.get('password')
    det={'Rollno':Rollno,'password':password}
    token = requests.post("https://shruthiapi.herokuapp.com/user_login",det)
    global p
    p = token.json()['access_token']
    Rollno=request.POST.get('rno')
    data = requests.get("http://shruthiapi.herokuapp.com/user_details",headers = {'Authorization':f'Bearer {p}'},msg={'Rollno':Rollno}) 
    res = data.json()
    context={'data': res} 
    return render(request,'api.html',context)



    