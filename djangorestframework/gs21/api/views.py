# Basic Authentication applied locally

from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # authentication_classes=[BasicAuthentication] Basic Authentication applied locally when uncomment this
    # permission_classes=[IsAuthenticated] Basic Authentication applied locally when uncomment this