import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Business(models.Model):
    Business_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Business_Name   =   models.TextField()
    Phone_Number    =   models.TextField()
    Industry    =   models.TextField()
    Email   =   models.EmailField()
    Director_First_Name =   models.TextField()
    Directors_Last_Name =   models.TextField()
    Directors_Other_Name    =   models.TextField()
    Directors_Phone_Number  =   models.TextField()
    Director_Email  = models.EmailField()
    Time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Business_Name
