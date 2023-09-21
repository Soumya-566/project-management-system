from django.db import models

# Create your models here.
class Student(models.Model):
	username=models.CharField(max_length=50,default="",primary_key=True)
	password=models.CharField(default=11,max_length=15)
	nameoffaculty=models.CharField(max_length=30)
	projectstatus=models.CharField(max_length=90000,default='')
	query=models.CharField(max_length=10000,default='')
	feedback=models.CharField(max_length=90000,default='')
	projectname=models.CharField(max_length=90000,default='')
	date=models.CharField(max_length=30,default='')
	
	
class Faculty(models.Model):
	username=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(default=15,max_length=15)
	areasofexpertise=models.CharField(max_length=100,default="")
	Mobileno=models.CharField(max_length=60,default=10)
	Emailid=models.CharField(max_length=50,default="")
class Admin(models.Model):
	username=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)