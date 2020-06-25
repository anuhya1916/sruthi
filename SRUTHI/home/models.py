from django.db import models
from user.models import User,Event
# Create your models here.


class Requests(models.Model):
       event_head_name=models.CharField(max_length=10)
       event_head_year=models.IntegerField()
       event_desc=models.CharField(max_length=400)
       email_id=models.CharField(max_length=40)
       
class Event_Head(models.Model):
       password=models.CharField(max_length=20)
       name=models.CharField(max_length=20)
       Rollno=models.IntegerField()
       Branch=models.CharField(max_length=10)
       year=models.IntegerField()
       mobile_no=models.IntegerField()
       email_id=models.CharField(max_length=40)
       event_id=models.IntegerField()
       
class events_interested(models.Model):
       user_id= models.ForeignKey(User, on_delete=models.CASCADE)
       event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
