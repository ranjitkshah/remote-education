from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
   first_name=models.CharField(max_length=150,blank=True)
   


    