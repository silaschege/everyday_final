from job_application.models import (
                    Applicant,
                    Guarantors,
                    Job_listing,
                    Application_made,
                    )
from .serializers import (
                    Applicant_Serializer,
                    Guarantors_Serializer,
                    Job_listing_Serializer,
                    Application_made_Serializer
                    )
from rest_framework import viewsets

class Applicant_viewset(viewsets.ModelViewSet):
    serializer_class    =   Applicant_Serializer
    queryset    =   Applicant.objects.all()

class Guarantors_viewset(viewsets.ModelViewSet):
    serializer_class    =   Guarantors_Serializer
    queryset    =   Guarantors.objects.all()


class Job_listing_viewset(viewsets.ModelViewSet):
    serializer_class    =   Job_listing_Serializer
    queryset    =   Job_listing.objects.all()

class Application_made_viewset(viewsets.ModelViewSet):
    serializer_class    =   Application_made_Serializer
    queryset    =   Application_made.objects.all()