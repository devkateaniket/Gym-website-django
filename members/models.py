from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
	PLAN_CHOICES = [
		('basic', 'Basic'),
		('standard', 'Standard'),
		('premium', 'Premium'),
	]
	GENDER_CHOICES = [
		('male', 'Male'),
		('female', 'Female'),
		('other', 'Other'),
	]

	full_name = models.CharField(max_length=120)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	address = models.TextField()
	plan_choice = models.CharField(max_length=20, choices=PLAN_CHOICES)
	join_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.full_name} ({self.plan_choice})"


class CustomerLoginActivity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_activities')
	login_at = models.DateTimeField(auto_now_add=True)
	ip_address = models.GenericIPAddressField(null=True, blank=True)
	user_agent = models.CharField(max_length=255, blank=True)

	class Meta:
		ordering = ['-login_at']
		verbose_name_plural = 'Customer login activities'

	def __str__(self):
		return f"{self.user.username} - {self.login_at:%Y-%m-%d %H:%M:%S}"
