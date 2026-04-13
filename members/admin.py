from django.contrib import admin
from .models import Customer, CustomerLoginActivity


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email', 'phone', 'plan_choice', 'join_date')
	search_fields = ('full_name', 'email', 'phone')
	list_filter = ('plan_choice', 'gender', 'join_date')


@admin.register(CustomerLoginActivity)
class CustomerLoginActivityAdmin(admin.ModelAdmin):
	list_display = ('user', 'login_at', 'ip_address')
	search_fields = ('user__username', 'user__email', 'ip_address')
	list_filter = ('login_at',)
