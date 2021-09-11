from business.models import (
                    Business,
                    )
from .serializers import (
                    Business_Serializer,
                    )
from rest_framework import viewsets

class Business_viewset(viewsets.ModelViewSet):
    serializer_class    =   Business_Serializer
    queryset    =   Business.objects.all()