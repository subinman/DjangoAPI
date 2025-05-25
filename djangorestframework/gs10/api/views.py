from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.query_params.get('id')
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializers(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student created', 'data': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student updated', 'data': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        stu.delete()
        return Response({'message': 'Student deleted successfully'})
