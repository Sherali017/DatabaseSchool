# from django.db import models
#
# SEMESTERS = (
#     ('fall', 'Fall'),
#     ('spring', 'Spring')
# )
#
#
# class YearModel(models.Model):
#     year = models.IntegerField(primary_key=True)
#
#
# class SemesterModel(models.Model):
#     year = models.ForeignKey(YearModel, on_delete=models.PROTECT())
#     title = models.CharField(max_length=100, choices=SEMESTERS)
#
#
# class SubjectModel(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class ProfessorModel(models.Model):
#     title = models.CharField(max_length=100)
#     teaches = models.ManyToManyField(SubjectModel)
#
#
# class MainModel(models.Model):
#     semester = models.ForeignKey(SemesterModel)
#     professor = models.ForeignKey(ProfessorModel)
#     subject = models.ForeignKey(SubjectModel)
#
#
# class StudentModel(models.Model):
#     title = models.CharField(max_length=100)
#
#
# class TakesModel(models.Model):
#     student = models.ForeignKey(StudentModel)
#     subject = models.ForeignKey(SubjectModel)
#     grade = models.IntegerField(null=True, blank=True)
