

from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    aadhar_number = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.address}, {self.phone_number}, {self.date_of_birth}, {self.gender}, {self.aadhar_number}"



class Help(models.Model):
    name_of_scheme = models.CharField(max_length=200)
    report_problem = models.CharField(max_length=500)

class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    suggested = models.CharField(max_length=500)
