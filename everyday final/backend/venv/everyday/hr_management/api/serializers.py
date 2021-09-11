from rest_framework import serializers
from hr_management.models import (
                    Employee,
                    Work_day,
                    Complain,
                    Announcement,
                    Issue,
                    Task
                    )




class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Employee
        fields  =   '__all__'

class Work_day_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Work_day
        fields  =   '__all__'

class Complain_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Complain
        fields  =   '__all__'


class Announcement_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Announcement
        fields  =   '__all__'

class Issue_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Issue
        fields  =   '__all__'

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Task
        fields  =   '__all__'