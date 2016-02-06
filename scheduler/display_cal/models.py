from django.db import models

#from django.conf import settings
#settings.configure()

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, default='')
    other = models.TextField()
    
    def __unicode__(self):
        return self.name

class Course(models.Model):
    codeNumber = models.CharField(max_length=8, default='')
    name = models.CharField(max_length=70)
    building = models.CharField(max_length=20)
    room = models.CharField(max_length=50)
    people = models.ManyToManyField(Person)
    
    def __unicode__(self):
        return self.name
    
class Period(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()
    day = models.CharField(max_length=2, default='NA')
    courses = models.ManyToManyField(Course)
    def __unicode__(self):
        return "{0}: {1}, {2}".format(self.day, self.startTime, self.endTime)
