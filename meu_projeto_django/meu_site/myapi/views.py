from django.shortcuts import render
from rest_framework import viewsets
from .models import UserSubmission
from .serializers import UserSubmissionSerializer

class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer

def index(request):
    return render(request, 'index.html')
