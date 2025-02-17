from django.db import models

from users.models import User

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class StudentAttendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)  # Presente, Falta...


class GradeLevel(models.Model):
    level = models.CharField(max_length=20)  # 1º ano, 2º ano, 3º ano...
    type = models.CharField(max_length=20)  # Infantil, Fundamental, Médio...


class Class(models.Model):
    grade_level_id = models.ForeignKey(GradeLevel, on_delete=models.CASCADE)
    academic_year = models.DateField()


class StudentClass(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    effective_date = models.DateField()
    status = models.CharField(max_length=20)  # Ativo, Transferido...


class Subject(models.Model):
    name = models.CharField(max_length=20)  # Portugues, Matematica...


class ClassSchedule(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)
    shift = models.CharField(max_length=20)
    subject_id = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()


class StudentGrade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20)  # Selecionar Bimestre 1, 2...
    type = models.CharField(max_length=20)  # Prova 1 , 2 ou 3, média
    score = models.CharField(max_length=4)  # ex: 9.7
