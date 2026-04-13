from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import redirect, render

from .forms import CustomerForm, SignupForm
from .models import CustomerLoginActivity


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		return x_forwarded_for.split(',')[0].strip()
	return request.META.get('REMOTE_ADDR')


def signup_view(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created successfully. Please login to continue.')
			return redirect('login')
	else:
		form = SignupForm()

	return render(request, 'signup.html', {'form': form})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			CustomerLoginActivity.objects.create(
				user=user,
				ip_address=get_client_ip(request),
				user_agent=request.META.get('HTTP_USER_AGENT', '')[:255],
			)
			return redirect('home')
	else:
		form = AuthenticationForm()

	return render(request, 'login.html', {'form': form})


@login_required
def home(request):
	return render(request, 'home.html')


@login_required

def join_gym(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()  # save and get object

            # Get user email (make sure your model has email field)
            user_email = customer.email
            user_name = customer.full_name  # adjust field name if different

            # Send confirmation email
            send_mail(
                subject='Gym Registration Successful',
                message=f'Hi {user_name},\n\nYour registration is successful! We will contact you soon.\n\nThank you!',
                from_email='your_email@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
            )

            messages.success(request, 'Registration submitted successfully. We will contact you soon.')
            return redirect('join_gym')
    else:
        form = CustomerForm()

    return render(request, 'join.html', {'form': form})


def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out successfully.')
	return redirect('login')
