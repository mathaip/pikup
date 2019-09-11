from django.shortcuts import render, redirect

from django.conf import settings

from django.http import HttpResponse

from django.conf.urls.static import static

from . import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
"""
message.info
message.success
message.warning
"""
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request,'landingpage/land-page.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'account created for{username}!')
			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username = username, password = password)
				login(request, user)
				return HttpResponseRedirect('/profile')
			else:
				raise forms.ValidationError('Looks like a username with that email or password already exists')
	else:
		form = UserRegisterForm()
	return render(request, 'registration/registration_form.html',{"form":form})



def pprofile(request):
    return render(request, 'passenger/profile.html')


def login(request):

	return render(request,'registration/login.html')
def logout (request):
	return 





