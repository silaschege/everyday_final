from .views import (                  
                    Employee_viewset,
                    Work_day_viewset,
                    Complain_viewset,
                    Announcement_viewset,
                    Issue_viewset,
                    Task_viewset
                    )
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Employee',Employee_viewset, basename='Employee')
router.register(r'Work_day',Work_day_viewset, basename='Work_day')
router.register(r'Complain',Complain_viewset, basename='Complain')
router.register(r'Announcement', Announcement_viewset, basename='Announcement')
router.register(r'Issue',Issue_viewset, basename='Issue')
router.register(r'Task',Task_viewset, basename='Task')
urlpatterns = router.urls