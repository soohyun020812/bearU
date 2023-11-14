from django.db import models
from django.contrib.auth.models import AbstractUser
# import basic user model

class User(AbstractUser):
    # How to specify a PK
    # user_id = models.AutoField(primary_key=True)
    # If do not declare a PK, Django will create it
    nickname = models.CharField(max_length = 30) # add nickname field

    class Meta: 
        db_table = "user" # table name "user"
