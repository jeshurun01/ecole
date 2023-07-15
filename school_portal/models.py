from django.db import models
import datetime


# Students Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Student: {self.name}>"
    
    def age(self):
        return int((datetime.date.today() - self.birth_date).days / 365.25)


# Teachers Model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Teacher: {self.name}>"

    def age(self):
        return int((datetime.date.today() - self.birth_date).days / 365.25)


# Classes Model
class Class(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Class: {self.name}>"

    def students_count(self):
        return self.students.count()


# Subjects Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Subject: {self.name}>"

    def classes_count(self):
        return self.classes.count()


# Assigment Model
class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    due_date = models.DateField()
    points = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


# Marks Model
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.name + ' ' + self.subject + ' ' + self.assignment + ' ' + str(self.score)



