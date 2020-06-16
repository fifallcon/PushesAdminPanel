from django.db import models


class Options(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    value = models.BooleanField()


class Pushes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    released = models.DateField()
    is_released = models.BooleanField()
    released_cnt = models.IntegerField()