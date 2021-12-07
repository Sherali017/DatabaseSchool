from rest_framework import serializers

from dbschool.models import TeacherModel, StudentModel


class TeacherModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeacherModel
		fields = '__all__'


class StudentModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentModel
		fields = '__all__'
