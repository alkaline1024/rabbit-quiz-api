from django.shortcuts import render
from django.db.models import query
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import *
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.http import Http404, HttpResponseNotFound  
from django.db.models import fields
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django_filters.filters import DateTimeFilter
from rest_framework import generics, viewsets, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.fields import datetime
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse

from api.models import Assignment, AssignmentStatus
from .serializers import *



class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Classroom.objects.all()

# class StudentViewSet(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         return Student.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Assignment.objects.all()

class AssignmentStatusViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentStatusSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return AssignmentStatus.objects.all()


@api_view(['POST'])
def user_result_do(request,pk):
    snippets = AssignmentStatus.objects.filter(id=pk)
    if(len(snippets) > 0):
        snippet = snippets[0]
        snippet.status = True
        snippet.save()
        return Response({"data": {"status": snippet.status}})
    else:
        return HttpResponseNotFound()

@api_view(['GET'])
def UserDetail(request):
    s = UserSerializer(request.user)
    return Response(s.data)

# @api_view(['POST'])
# def addUser(request,pk):
#     data = request.data
#     NewMember = data['new']
#     NewUser = User.objects.get(username=NewMember)
#     NewUser.save()
#     a1 = Classroom.objects.filter(id=pk)
#     a1 = Classroom()
#     a1.Member.add(NewUser)


#     return Response({"New": ClassMember.Member})

@api_view(['POST'])
def addUser(request,pk):
    data = request.data
    NewMember = data['user']
    newuser = User.objects.get(username=NewMember)
    classroom = Classroom.objects.get(id=pk)
    classroom.Member.add(newuser)

    return Response({"success"})

@api_view(['POST'])
def removeUser(request,pk):
    data = request.data
    inUser = data['user']
    inuser = User.objects.get(username=inUser)
    classroom = Classroom.objects.get(id=pk)
    classroom.Member.remove(inuser)

    return Response({"success"})

