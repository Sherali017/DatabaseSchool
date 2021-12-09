from django.db import models
from address.models import SchoolModel
import datetime
from dbschool.choices import *


class QuartersModel(models.Model):
    year = models.CharField(max_length=255,
                            default=f'{datetime.date.today().year}/{datetime.date.today().year + 1}')
    title = models.CharField(max_length=100, choices=QUARTERS)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.year}-yil {self.title}'

    class Meta:
        verbose_name = 'chorak'
        verbose_name_plural = 'chorak'


class SubjectModel(models.Model):
    title = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'fan'
        verbose_name_plural = 'fanlar'


class ClassesModel(models.Model):
    class_code = models.CharField(max_length=255)

    def __str__(self):
        return self.class_code

    class Meta:
        verbose_name = 'Sinf'
        verbose_name_plural = 'Sinflar'


class TeacherModel(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.PROTECT)
    subject = models.ManyToManyField(SubjectModel)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"


class StudentModel(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True)
    ball = models.IntegerField(null=True)
    date_of_birth = models.DateField()
    school = models.ForeignKey(SchoolModel, on_delete=models.PROTECT)
    current_class = models.ForeignKey(ClassesModel, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.other_name}'

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'talabalar'


class TakesModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.PROTECT)
    subject = models.ForeignKey(SubjectModel, on_delete=models.PROTECT)
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} {self.grade}'

    class Meta:
        verbose_name = 'Baho'
        verbose_name_plural = 'Baholar'


class DarsJadvaliModel(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.PROTECT)
    quarter = models.ManyToManyField(QuartersModel)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.PROTECT)
    schclass = models.ForeignKey(ClassesModel, on_delete=models.PROTECT)
    week = models.CharField(max_length=100, choices=DAYS_OF_WEEK)
    hour = models.CharField(max_length=100, choices=hour)

    subject = models.ForeignKey(SubjectModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.schclass

    class Meta:
        verbose_name = 'Dars jadvali'
        verbose_name_plural = 'Dars jadvallari'


