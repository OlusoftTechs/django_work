from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Age = models.CharField(max_length=255)
  Phone = models.CharField(max_length=255)
  joined_date = models.DateField(null=True)
  nationality = models.CharField(null=True, max_length=255)
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}"