from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView

from address.models import VilAddressModel, TShAddressModel, SchoolAddressModel
from api.serializers import TeacherModelSerializer, StudentModelSerializer, VilAddressModelSerializer, \
	TShAddressModelSerializer, SchoolAddressModelSerializer, ClassesModelSerializer, TakesModelSerializer
from dbschool.models import TeacherModel, StudentModel, ClassesModel, TakesModel


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


#####################################################
class VilAddressModelListAPIView(ListAPIView):
	queryset = VilAddressModel.objects.all()
	serializer_class = VilAddressModelSerializer


class VilAddressModelCreateAPIView(CreateAPIView):
	queryset = VilAddressModel.objects.all()
	serializer_class = VilAddressModelSerializer


class VilAddressModelUpdateAPIView(UpdateAPIView):
	queryset = VilAddressModel.objects.all()
	serializer_class = VilAddressModelSerializer


class VilAddressModelDeleteAPIView(DestroyAPIView):
	queryset = VilAddressModel.objects.all()
	serializer_class = VilAddressModelSerializer


class TShAddressModelListAPIView(ListAPIView):
	queryset = TShAddressModel.objects.all()
	serializer_class = TShAddressModelSerializer


class TShAddressModelCreateAPIView(CreateAPIView):
	queryset = TShAddressModel.objects.all()
	serializer_class = TShAddressModelSerializer


class TShAddressModelUpdateAPIView(UpdateAPIView):
	queryset = TShAddressModel.objects.all()
	serializer_class = TShAddressModelSerializer


class TShAddressModelDeleteAPIView(DestroyAPIView):
	queryset = TShAddressModel.objects.all()
	serializer_class = TShAddressModelSerializer


class SchoolAddressModelListAPIView(ListAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelCreateAPIView(CreateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelUpdateAPIView(UpdateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelDeleteAPIView(DestroyAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer

###############################################################################################################


class ClassesModeListAPIView(ListAPIView):
	queryset = ClassesModel.objects.all()
	serializer_class = ClassesModelSerializer


class ClassesModelCreateAPIView(CreateAPIView):
	queryset = ClassesModel.objects.all()
	serializer_class = ClassesModelSerializer


class ClassesModelUpdateAPIView(UpdateAPIView):
	queryset = ClassesModel.objects.all()
	serializer_class = ClassesModelSerializer


class ClassesModelDeleteAPIView(DestroyAPIView):
	queryset = ClassesModel.objects.all()
	serializer_class = ClassesModelSerializer


class TakesModelListAPIView(ListAPIView):
	queryset = TakesModel.objects.all()
	serializer_class = TakesModelSerializer


class TakesModelCreateAPIView(CreateAPIView):
	queryset = TakesModel.objects.all()
	serializer_class = TakesModelSerializer


class TakesModelUpdateAPIView(UpdateAPIView):
	queryset = TakesModel.objects.all()
	serializer_class = TakesModelSerializer


class TakesModelDeleteAPIView(DestroyAPIView):
	queryset = TakesModel.objects.all()
	serializer_class = TakesModelSerializer


class SchoolAddressModelListAPIView(ListAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelCreateAPIView(CreateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelUpdateAPIView(UpdateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelDeleteAPIView(DestroyAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelListAPIView(ListAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelCreateAPIView(CreateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelUpdateAPIView(UpdateAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer


class SchoolAddressModelDeleteAPIView(DestroyAPIView):
	queryset = SchoolAddressModel.objects.all()
	serializer_class = SchoolAddressModelSerializer
