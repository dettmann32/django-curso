from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class SuCasa(models.Model):

    cor = models.CharField(max_length=255)
    numero = models.IntegerField

