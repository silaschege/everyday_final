from rest_framework import serializers
from business.models import (
                    Business,
)


class Business_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Business
        fields  =   '__all__'