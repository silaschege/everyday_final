from .views import (
                    Applicant_viewset,
                    Guarantors_viewset,
                    Job_listing_viewset,
                    Application_made_viewset,
                    )
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Applicant',Applicant_viewset, basename='Applicant')
router.register(r'Guarantors',Guarantors_viewset, basename='Guarantors')
router.register(r'Listing',Job_listing_viewset, basename='Job_listing')
router.register(r'Applications',Application_made_viewset, basename='Applications_made')
urlpatterns = router.urls