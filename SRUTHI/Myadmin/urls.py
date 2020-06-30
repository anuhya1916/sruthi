from django.urls import path

from . import views

urlpatterns = [
    path('',views.Myadmin, name='Myadmin'),
    path('admin-login',views.admin_login, name='admin_login'),
    path('accept/<int:req_id>/',views.accept,name='accept'),
    path('reject/<int:req_id>/',views.reject,name='reject'),
    path('delete/<int:Rollno>/',views.delete,name='delete'),
]