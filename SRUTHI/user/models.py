from django.db import models

# Create your models here.
class User(models.Model):
       password=models.CharField(max_length=20)
       name=models.CharField(max_length=20)
       Rollno=models.IntegerField()
       college=models.CharField(max_length=20)
       branch=models.CharField(max_length=10)
       year=models.IntegerField()
       mobile_no=models.IntegerField()
       email_id=models.CharField(max_length=40)
       
class Event(models.Model):
       event_title=models.CharField(max_length=20)
       event_head_id=models.IntegerField()
       event_desc =models.CharField(max_length=500)
       event_location=models.CharField(max_length=30)
       event_datetime=models.DateField
       event_dept=models.CharField(max_length=10)
       budget_expected=models.IntegerField()
       actual_budget=models.IntegerField()


class registrations(models.Model):
       user_id= models.ForeignKey(User, on_delete=models.CASCADE)
       event_id=models.ForeignKey(Event, on_delete=models.CASCADE)
       

    