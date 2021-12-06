from rest_framework import serializers

from dbschool.models import TeacherModel


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'