from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSubmissionViewSet
from .views import index 
router = DefaultRouter()
router.register(r'submissions', UserSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', index, name='index'),
]
