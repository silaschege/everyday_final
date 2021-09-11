import uuid
from django.db import models
from django.utils import timezone
from business.models import Business
from django.conf import settings

# Create your models here.
class Applicant (models.Model):
    Applicant_Id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name   =   models.TextField()
    Last_Name   =   models.TextField()
    Other_Names   =   models.TextField()
    Email   =   models.EmailField()
    Date_of_birth   =   models.DateField()
    Id_Number   =   models.TextField()
    Phone_Number   =   models.TextField()
    Level_of_Education   =   models.TextField()
    Course   =   models.TextField()
    Other_Education   =   models.TextField()
    Previous_Job   =   models.TextField()
    Time_Worked_There   =   models.IntegerField()

    def __str__(self):
        return self.First_Name

class Guarantors (models.Model):
    Guarantors_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_name   =   models.TextField()
    Last_name   =   models.TextField()
    Other_Names   =   models.TextField()
    Email   =   models.EmailField()
    Id_Number   =   models.TextField()
    Phone_Number   =   models.TextField()
    Relationship   =   models.TextField()   
    Applicant   =   models.ForeignKey(Applicant,on_delete=models.CASCADE)
    

class  Job_listing (models.Model):
    Job_listing_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Education_level   =   models.TextField()
    Course   =   models.TextField()
    Years_experience    =   models.IntegerField()
    End_of_application_date =   models.DateField()
    Position   =   models.TextField()
    Location   =   models.TextField()
    Business    =   models.ForeignKey(Business,on_delete=models.CASCADE)


    

class Application_made (models.Model):
    Application_made_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Applicant   =   models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applicant')
    Job_listing   =   models.ManyToManyField(Job_listing)
    Time = models.DateTimeField(default=timezone.now)
    