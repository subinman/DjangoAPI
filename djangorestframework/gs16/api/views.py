# Concrete View Class in Django

from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView



class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers