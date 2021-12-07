from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView

from api.serializers import TeacherModelSerializer
from dbschool.models import TeacherModel


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
