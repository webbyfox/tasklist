from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from .models import Task
# from .serializers import TaskSerializer


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)




@api_view(['GET', 'PUT', 'POST'])
@permission_classes((permissions.AllowAny,))
@method_decorator(csrf_exempt)
def task_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','POST' 'DELETE'])
@permission_classes((permissions.AllowAny,))
@method_decorator(csrf_exempt)
@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a task instance.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def task_detail(request, pk):
#         """
#         Retrieve, update or delete a code task.
#         """
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return HttpResponse(status=404)
#
#         if request.method == 'GET':
#             serializer = TaskSerializer(task)
#             return JSONResponse(serializer.data)
#
#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = TaskSerializer(task, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JSONResponse(serializer.data)
#             return JSONResponse(serializer.errors, status=400)
#
#         elif request.method == 'DELETE':
#             task.delete()
#             return HttpResponse(status=204)
