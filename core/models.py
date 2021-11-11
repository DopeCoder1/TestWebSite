from django.db import models


# Create your models here.
class RegisterStudent(models.Model):
    teamName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number = models.BigIntegerField(unique=True)
    fioOne = models.CharField(max_length=255)
    fioSecond = models.CharField(max_length=255)
    fioThree = models.CharField(max_length=255, blank=True)
    fioFour = models.CharField(max_length=255, blank=True)
    fioFive = models.CharField(max_length=255, blank=True)
    university_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.teamName
