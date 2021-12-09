from rest_framework import serializers

from address.models import VilAddressModel, TShAddressModel, SchoolAddressModel, SchoolModel
from dbschool.models import TeacherModel, StudentModel, QuartersModel, SubjectModel, ClassesModel, TakesModel, \
	MainModel, DarsJadvaliModel
from staff.models import DirektorModel, KuratorModel


class TeacherModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeacherModel
		fields = '__all__'


class StudentModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentModel
		fields = '__all__'


class VilAddressModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = VilAddressModel
		fields = '__all__'


class TShAddressModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TShAddressModel
		fields = '__all__'


class SchoolAddressModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchoolAddressModel
		fields = '__all__'


class SchoolModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchoolModel
		fields = '__all__'


class QuartersModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = QuartersModel
		fields = '__all__'


class SubjectModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubjectModel
		fields = '__all__'


###############!!!
class ClassesModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClassesModel
		fields = '__all__'


class TakesModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TakesModel
		fields = '__all__'


class DarsJadvaliModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = DarsJadvaliModel
		fields = '__all__'


class DirektorModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = DirektorModel
		fields = '__all__'


class KuratorModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = KuratorModel
		fields = '__all__'
