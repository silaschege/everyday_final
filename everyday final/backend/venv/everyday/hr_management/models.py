import uuid
from django.db import models
from django.utils import timezone
from business.models import Business
from django.conf import settings


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
    Business    =   models.ForeignKey(Business,on_delete=models.CASCADE)

    def __str__(self):
        return self.Post

class Work_day(models.Model):
    Work_day_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date    =   models.DateField()
    Business    =   models.ForeignKey(Business,on_delete=models.CASCADE)
    Employee =  models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_workday')

class Announcement(models.Model):
    Communication_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Message =   models.TextField()
    From    =   models.TextField()
    To  =   models.TextField()
    Business_hr    =   models.ForeignKey(Business,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_announcements')
    Time = models.DateTimeField(default=timezone.now)


class Issue(models.Model):
    Issue_Id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Date    =   models.DateField()
    Disciplinary_Action =   models.TextField()
    Action_Taken    =   models.TextField()
    Business    =   models.ForeignKey(Business,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_issue')
    Time = models.DateTimeField(default=timezone.now)

class Complain(models.Model):
    Complain_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Date    =   models.DateField()
    Disciplinary_Action =   models.TextField()
    Action_Taken    =   models.TextField()
    Business_hr    =   models.ForeignKey(Business,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_complains')
    Time = models.DateTimeField(default=timezone.now)

class Task (models.Model):
    Task_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Task    =   models.TextField()
    State   =   models.BooleanField()
    From    =   models.TextField()
    Date    =   models.DateField()
    Business    =   models.ForeignKey(Business,on_delete=models.CASCADE)
    Employee =  models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_tasks')
    Time = models.DateTimeField(default=timezone.now)


