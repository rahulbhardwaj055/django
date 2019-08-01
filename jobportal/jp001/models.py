from django.db import models

# Create your models here.

class indiaJob(models.Model):
    empname=models.CharField(max_length=30)
    empexp=models.IntegerField()
    empskills=models.CharField(max_length=30)
    empphone=models.IntegerField()
'''
def __str__(self):
    return 'Employee Object with eno: +str(self.no)'
'''

class indiaJob1(models.Model):
    empname=models.CharField(max_length=30)
    empexp=models.IntegerField()
    empskills=models.CharField(max_length=30)
    empphone=models.IntegerField()

class indiaJob2(models.Model):
    empname=models.CharField(max_length=30)
    empexp=models.IntegerField()
    empskills=models.CharField(max_length=30)
    empphone=models.IntegerField()

class indiaJob3(models.Model):
    empname=models.CharField(max_length=30)
    empexp=models.IntegerField()
    empskills=models.CharField(max_length=30)
    empphone=models.IntegerField()
