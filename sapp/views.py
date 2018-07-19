
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import servicer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .forms import CustomUserCreationForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings


def home(request):
	return render(request, 'sapp/front end.html')


def results(request):
	if 'q' in request.GET and request.GET['q'] and 'p' in request.GET and request.GET['p'] and 'r' in request.GET and request.GET['r']:
		q = request.GET['q']
		p = request.GET['p']
		r = request.GET['r']
		service = servicer.objects.filter(locality__icontains=q, service__icontains=p, city__icontains=r)
		return render(request, 'sapp/results.html', {'service' :service , 'locality': q, 'type':p, 'city':r})
	else:
		return HttpResponseRedirect('Please type a locality')

def register(request):
	if request.method == 'POST':
		f = CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, 'Account created successfully')
			return redirect('register')

	else:
		f = CustomUserCreationForm()

	return render(request, 'sapp/register.html', {'form': f})

def login(request):
	if request.method == 'POST':
		login = request.POST.get('usr')
		if login == "provider":
			return redirect('prologin')
		else:
			return redirect('userlogin')

	return render(request, 'sapp/login.html')

def userlogin(request):
	if request.user.is_authenticated :
		return redirect('user_page')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			# correct username and password login the user
			auth.login(request, user)
			return redirect('user_page')

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'sapp/userlogin.html')

def prologin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		ser = servicer.objects.filter(email_id=username, password=password)

		if ser is not None:
			# correct username and password login the user
			return redirect('provider_page')

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'sapp/servicer-login.html')


def logout(request):
	auth.logout(request)
	return render(request,'sapp/logout.html')


def user_page(request):
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'sapp/admin_page.html')

def provider_page(request):
	return render(request, 'sapp/admin_page.html')


def contribute(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		mobile_no = request.POST.get('mobile_no')
		service = request.POST.get('service')
		locality = request.POST.get('locality')
		city = request.POST.get('city')
		email_id = request.POST.get('email_id')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		r = servicer.objects.filter(email_id=email_id)
		if r.count():
			raise  ValidationError("service provider already exists")

		if password1 != password2:
			raise  ValidationError("password doesn't match")

		s = servicer()
		s.name = name
		s.mobile_no = mobile_no
		s.service = service
		s.locality = locality
		s.city = city
		s.email_id = email_id
		s.password = password1
		s.save() 
		return HttpResponseRedirect('a new contributor')

	else:
		return render(request, 'sapp/contribute.html')

def book(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			email = request.POST.get('email')
			subject = 'Service Booking'
			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email,email]
			contact_message = "Need to book you for a service.\nClick the link below to confirm." 

			send_mail(
    		subject,
    		contact_message,
    		from_email,
    		to_email,
    		fail_silently=False,
			)

		return render(request, 'sapp/mail.html', {'email' :email})
	else:
		return redirect('login')





		
 
   
	  