from django.db import models


class Customer(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=256)

	def register(self):
		return self.save()


	@staticmethod
	def get_customer_by_email(email):
		try:
			return Customer.objects.get(email=email)
		except:
			return False


	def isExists(self):
		if Customer.objects.filter(email=self.email):
			return True
		else:
			return False


	def __str__(self):
		return f"{self.first_name} {self.last_name}"
