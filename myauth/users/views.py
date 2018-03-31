from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
	next = request.GET.get('next', request.POST.get('next', ''))
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			if next:
				return redirect(next)
			return redirect('/')
	
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', context={'form': form, 'next': next})
	
def index(request):
	return render(request, 'index.html')
