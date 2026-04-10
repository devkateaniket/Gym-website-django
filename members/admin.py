from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email', 'phone', 'plan_choice', 'join_date')
	search_fields = ('full_name', 'email', 'phone')
	list_filter = ('plan_choice', 'gender', 'join_date')
