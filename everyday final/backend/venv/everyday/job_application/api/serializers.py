from rest_framework import serializers
from job_application.models import (
                    Applicant,
                    Guarantors,
                    Job_listing,
                    Application_made,
                    )


class Applicant_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Applicant
        fields  =   '__all__'

class Guarantors_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Guarantors
        fields  =   '__all__'


class Job_listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Job_listing
        fields  =   '__all__'

class Application_made_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Application_made
        fields  =   '__all__'


