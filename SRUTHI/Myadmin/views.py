from django.shortcuts import render
import requests
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import json
from django.http import HttpResponse

# Create your views here.
def Myadmin(request):
    return render(request,'admin-login.html',None)

def admin_login(request):
    admin_id=request.POST.get('admin_id')
    password=request.POST.get('pwd')
    det={"admin_id":admin_id,"password":password}
    token = requests.post("https://shruthiapi.herokuapp.com/admin_login",det)
    if(token.status_code== 200):
        global p
        p = token.json()
        headers = {"Authorization": "Bearer "  + p['access_token']}
        td = requests.get("https://shruthiapi.herokuapp.com/requests",headers=headers) 
        res = td.json()
        td1 = requests.get("https://shruthiapi.herokuapp.com/view_user",headers=headers) 
        res1 = td1.json()
        context={'request_list': res,'users':res1,} 
        return render(request,'admin-page.html',context)
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'admin-login.html',context)
def reject(request,req_id):
    det={"admin_id":1,"password":'admin@123'}
    token = requests.post("https://shruthiapi.herokuapp.com/admin_login",det)
    if(token.status_code== 200):
        global p
        p = token.json()
        det1={'req_id':req_id}
        td = requests.post("https://shruthiapi.herokuapp.com/req_remove",det1,headers = {'Authorization':f'Bearer {p}'}) 
        return
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'admin-page.html',context)
def accept(request,req_id):
    str="admin@123"
    det={"admin_id":1,"password":str}
    token = requests.post("https://shruthiapi.herokuapp.com/admin_login",det)
    if(token.status_code== 200):
        global p
        p = token.json() 
        det1={'req_id':req_id}
        td = requests.post("http://shruthiapi.herokuapp.com/confirmation",det1,headers = {'Authorization':f'Bearer {p}'})
        return HttpResponse("Accepted")
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'admin-page.html',context)
def delete(request,Rollno):
    det={"admin_id":1,"password":'admin@123'}
    token = requests.post("https://shruthiapi.herokuapp.com/admin_login",det)
    if(token.status_code== 200):
        global p
        p = token.json() 
        det1={'Rollno':Rollno}
        td = requests.post("https://shruthiapi.herokuapp.com/user_remove",det1,headers = {'Authorization':f'Bearer {p}'})
        return redirect("http://127.0.0.1:8000/Myadmin/admin-login")
    else:
        messages="credentials invalid"
        context={'messages':messages}
        return render(request,'admin-login.html',context)


    
