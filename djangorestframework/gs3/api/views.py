from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import StudentSerializer
import json
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse , JsonResponse

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'Data Deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
    
