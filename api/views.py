from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializers import TeacherModelSerializer
from dbschool.models import TeacherModel


class TeacherListAPIView(ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherModelSerializer

