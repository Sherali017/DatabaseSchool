from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView

from api.serializers import TeacherModelSerializer, StudentModelSerializer
from dbschool.models import TeacherModel, StudentModel


class TeacherListAPIView(ListAPIView):
	queryset = TeacherModel.objects.all()
	serializer_class = TeacherModelSerializer


class TeacherCreateAPIView(CreateAPIView):
	queryset = TeacherModel.objects.all()
	serializer_class = TeacherModelSerializer


class TeacherUpdateAPIView(UpdateAPIView):
	queryset = TeacherModel.objects.all()
	serializer_class = TeacherModelSerializer


class TeacherDeleteAPIView(DestroyAPIView):
	queryset = TeacherModel.objects.all()
	serializer_class = TeacherModelSerializer


class StudentListAPIView(ListAPIView):
	queryset = StudentModel.objects.all()
	serializer_class = StudentModelSerializer


class StudentCreateAPIView(CreateAPIView):
	queryset = StudentModel.objects.all()
	serializer_class = StudentModelSerializer


class StudentUpdateAPIView(UpdateAPIView):
	queryset = StudentModel.objects.all()
	serializer_class = StudentModelSerializer


class StudentDeleteAPIView(DestroyAPIView):
	queryset = StudentModel.objects.all()
	serializer_class = StudentModelSerializer
