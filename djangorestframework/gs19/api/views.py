# Ready Only Model View Set

from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers