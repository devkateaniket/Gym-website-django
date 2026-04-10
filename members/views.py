from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CustomerForm


def home(request):
	return render(request, 'home.html')


def join_gym(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Registration submitted successfully. We will contact you soon.')
			return redirect('join_gym')
	else:
		form = CustomerForm()

	return render(request, 'join.html', {'form': form})
