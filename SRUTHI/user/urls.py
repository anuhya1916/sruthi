from django.urls import path

from . import views

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('user_login/api_call',views.api_call,name='api'),
    path('user_registration/registration',views.registration,name='registration')
]