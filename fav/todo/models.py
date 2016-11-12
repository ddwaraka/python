from __future__ import unicode_literals
# from datetime import date
from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_priority = models.CharField(max_length=10)
    task_status = models.CharField(max_length=20)
    target_date = models.DateField('date')

    def __unicode__(self):
        return "{0}, {1}, {2}, {3}".format(self.task_name, self.task_priority, self.task_status, self.target_date)


# return self.album_title + '-' + self.artist




