from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializers


class StudentAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk:
            stu = get_object_or_404(Student, id=pk)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student updated', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student partially updated', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        stu.delete()
        return Response({'message': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)
