from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):      #for tables of database
    title = models.CharField(max_length = 200)
    text = models.TextField()       #unlimited character option textfield()
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'notes') #to delete all notes id user is deleted
    