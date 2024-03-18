from django.db import models

# Create your models here.
class Notes(models.Model):      #for tables of database
    title = models.CharField(max_length = 200)
    text = models.TextField()       #unlimited character option textfield()
    created = models.DateTimeField(auto_now_add = True)