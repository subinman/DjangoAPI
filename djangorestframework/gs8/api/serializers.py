from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
       if value[0].lower()!='r':
              raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.ModelSerializer):
        class Meta:
                model=Student
                name=serializers.CharField(max_length=100, validators=[start_with_r])
                fields=['name','roll','city']

# Field Validation
def validate_roll(self, value):
        if value>=200:
                raise serializers.ValidationError('seat full')
        return value

# Object Level Validation
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
        raise serializers.ValidationError('City must be Ranchi if name is Rohit.')
    return data
               
      