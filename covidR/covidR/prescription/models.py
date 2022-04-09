from django.db import models
from random import choices
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other','Other')
    )
BLOOD = (
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+')

)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField('Address',max_length = 50)
    contact = models.IntegerField('Contact', validators = [MaxValueValidator(9999999999)])
    dob = models.DateField('Event Date')
    speciality = models.CharField('Speciality',max_length = 100)
    gender = models.CharField('Gender',max_length = 20, choices = GENDER)
    blood = models.CharField('Blood',max_length = 10, choices = BLOOD)
 
    def __str__(self):
        return self.user.username

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField('Address',max_length = 50)
    contact = models.IntegerField('Contact', validators = [MaxValueValidator(9999999999)])
    dob = models.DateField('Date of Birth')
    gender = models.CharField('Gender',max_length = 20,choices=GENDER)
    blood = models.CharField('Blood',max_length = 10,choices=BLOOD)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    name = models.CharField('Patient Name',max_length=30)
    email = models.EmailField('Email' ,max_length = 90)
    address = models.CharField('Address',max_length = 50)
    contact = models.IntegerField('Contact', validators = [MaxValueValidator(9999999999)])
    dob = models.DateField('Date of Birth')
    gender = models.CharField('Gender',max_length = 20, choices=GENDER)
    blood = models.CharField('Blood',max_length = 10,choices=BLOOD)

    def __str__(self):
        return self.name