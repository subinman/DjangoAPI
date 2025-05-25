# Model View Set 

from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers