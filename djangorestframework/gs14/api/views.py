# GenericGeneric API View and Mixins

from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentListCreateAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs) 
    
    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)  
    
class StudentRUDAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    lookup_field = 'id' 

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)  
    
    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)  
    


