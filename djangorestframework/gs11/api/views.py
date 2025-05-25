from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status


@api_view(['GET', 'POST', 'PUT','PATCH' 'DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        # id = request.query_params.get('id')
        id=pk
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializers(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        id=pk
        # id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student updated', 'data': serializer.data})
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        id=pk
        # id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializers(stu, data=request.data, partial=True)  # 🔑 partial=True
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student partially updated', 'data': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        id=pk
        # id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        stu.delete()
        return Response({'message': 'Student deleted successfully'})
