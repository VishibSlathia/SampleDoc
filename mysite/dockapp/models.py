from django.db import models

# Create your models here.
#provides ORM
class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

class ToListenSongs(models.Model):
    title = models.CharField(max_length = 200)
    listened = models.BooleanField(default = False)