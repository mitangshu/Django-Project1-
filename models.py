from django.db import models

# Create your models here.
class Register(models.Model):
	emailID = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	mobile = models.CharField(max_length = 200)
	Fullname = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)

def __str__(self):
	return self.emailID + " " + self.password + " " + self.mobile + " " + self.Fullname + " " + self.address 