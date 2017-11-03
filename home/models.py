from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class UserBio(models.Model):

	# this is just a sample

	username = models.CharField(max_length=200)
	age = models.CharField(max_length=100)
	tax_status = models.CharField(max_length=100)


	def get_absolute_url(self):
		return reverse('home:user_detail',  kwargs={'pk': self.pk})
	def __str__(self):
		return self.username

class UserTaxInfo(models.Model):
	userbio = models.ForeignKey(UserBio, on_delete=models.CASCADE)
	total_income = models.IntegerField()
	total_deductions = models.IntegerField()

	def get_absolute_url(self):
		return reverse('home:user_detail',  kwargs={'pk': self.pk})