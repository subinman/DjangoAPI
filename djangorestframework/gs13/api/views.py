# GenericGeneric API View and Mixins

from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs) 
    
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)  
    
class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    lookup_field = 'id'  # Tell the view to use 'student_id' from URL

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)
    
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 
    lookup_field = 'id'  # Tell the view to use 'student_id' from URL

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)  
    
class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers 
    lookup_field = 'id'  # Tell the view to use 'student_id' from URL

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)  

