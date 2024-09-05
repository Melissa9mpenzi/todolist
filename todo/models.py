from django.db import models
"""
family members, brief contacts.
capture their work and assign tasks to them.
there's a need for you to manage people at home and their work done respectively
this can be done by making corresponding models.

MODELS
familyMembers(name,contact, interests)
tasks(name, description, day of the week)
workDone(family_member, task, date_done)
"""

# Create your models here.
class Task(models.Model):
    DAYS_OF_WEEK = [('Monday','Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday','Thursday'), ('Friday','Friday'), ('Saturday','Saturday'), ('Sunday','Sunday')]
    name = models.CharField(max_length=50)
    description = models.TextField()
    day_of_the_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK, default='Monday')

    def __str__(self):
        return self.name

class FamilyMember(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=50)
    interests = models.TextField()

    def __str__(self):
        return self.name

class WorkDone(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_done = models.DateField()

    def __str__(self):
        return f"{self.family_member.name} did {self.task.name} on {self.date_done}"

   #task = (self.family_member.name) +"-"+ (self.task.name) + "-" + (self.date_done)
   #return f"{self.family_member.name} - {self.task.name} - {self.date_done}" def __str__(self):
     
class Parents(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    