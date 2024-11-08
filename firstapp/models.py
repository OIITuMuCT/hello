from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    object_person = models.Manager()
    DoesNotExist = models.Manager

    def __str__(self):
        return self.name


# One to many model example
class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name


# Many To Many model example
class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# One To One model example

class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


