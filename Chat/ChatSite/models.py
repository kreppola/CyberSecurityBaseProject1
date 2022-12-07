from django.db import models


# Create your models here.
class message(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user = models.CharField(max_length=200)
    room_nr = models.IntegerField(default=0)

class privateRoom(models.Model):
    member1 = models.CharField(max_length=200)
    member2 = models.CharField(max_length=200)
    pid = models.IntegerField(default=0)
