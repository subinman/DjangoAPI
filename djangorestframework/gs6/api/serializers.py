from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Student
                fields=['name','roll','city']
               
      

# class StudentSerializer(serializers.Serializer):
#         name=serializers.CharField(max_length=100)
#         roll=serializers.IntegerField()
#         city=serializers.CharField(max_length=100)

# def create(self, validate_data):
#         return Student.objects.create(**validate_data)

# def update(self, instance, validate_data):
#         instance.name=validate_data.get('name', instance.name)
#         instance.name=validate_data.get('roll', instance.roll)
#         instance.name=validate_data.get('city', instance.city)
#         instance.save()
#         return instance