from .views import (
                    Business_viewset,
                    )
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Business',Business_viewset, basename='Business_viewset')
urlpatterns = router.urls