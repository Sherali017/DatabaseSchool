from django.db import models


from address.models import SchoolModel
from dbschool.models import ClassesModel


class DirektorModel(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.PROTECT)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    class Meta:
        verbose_name = 'direktor'
        verbose_name_plural = 'direktorlar'


class KuratorModel(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.PROTECT)
    classes = models.OneToOneField(ClassesModel, on_delete=models.PROTECT)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Kurator'
        verbose_name_plural = 'kuratorlar'
