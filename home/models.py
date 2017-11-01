from django.db import models

# Create your models here.
class UserBio(models.Model):

	

	username = models.CharField(max_length=200)
	age = models.CharField(max_length=100)
	tax_status = models.CharField(max_length=100)

	def __str__(self):
		return self.username

class UserTaxInfo(models.Model):
    userbio = models.ForeignKey(UserBio, on_delete=models.CASCADE)
    total_income = models.IntegerField()
    total_deductions = models.IntegerField()
    
    def __str__(self):
    	return self.total_income

    	# this is the comment added to model
