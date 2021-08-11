from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("Home Page")

@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)