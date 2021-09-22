import uuid
from django.db import models
from django.utils import timezone
from business.models import Business
from django.conf import settings
import datetime


# Create your models here..

class Employee(models.Model):
    Employee_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_name  =   models.TextField()  
    Last_name   =   models.TextField() 
    Other_Names =   models.TextField()
    Id_Number   =   models.TextField()
    Phone_Number    =   models.TextField()
    Post    =   models.TextField()
    Company_Position    =   models.TextField()
  

    def __str__(self):
        return self.Post

class Work_day(models.Model):
    Work_day_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date    =   models.DateField(default=datetime.date.today)
    Employee = models.TextField()

class Announcement(models.Model):
    Communication_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Message =   models.TextField(default="Something")
    From    =   models.TextField(default="Something")
    To  =   models.TextField(default="Something")
    Time = models.DateTimeField(default=timezone.now)


class Issue(models.Model):
    Issue_Id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Date    =   models.DateField(default=datetime.date.today)
    Action =   models.TextField()
    


class Complain(models.Model):
    Complain_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Action =   models.TextField()
    Date    =   models.DateField(default=datetime.date.today)
 
  

class Task (models.Model):
    Task_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Task    =   models.TextField()
    State   =   models.TextField()
    From    =   models.TextField()
    Date    =   models.DateField(default=datetime.date.today)
    Time = models.DateTimeField(default=timezone.now)


