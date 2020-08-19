from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse  
from django.contrib import messages
from .models import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def home(request):
	return render(request,'home.html')

def signup(request):
	if request.method == "POST":
		full_name=request.POST["full_name"]
		username=request.POST["username"]
		email=request.POST["email"]
		password=request.POST["password"]

		first_name=full_name.split()[0]
		last_name=" ".join(full_name.split()[1:])

		user = User.objects.create_user(first_name=first_name,
										last_name=last_name,
										username=username,
										email=email,
										password=password)

		

		login(request,user)
		return redirect("/dashboard/")			
	return render(request,"signup.html")

def signin(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]

		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect("/dashboard/")

	return render(request,"signin.html")

def dashboard(request):
	return render(request,"dashboard.html")

def save(request):
	if request.method == "POST":
		location=request.POST["location"]
		incident_description=request.POST["incident_description"]
		date=request.POST["date"]
		time=request.POST["time"]
		incident_location=request.POST["incident_location"]
		initial_severity=request.POST["initial_severity"]
		suspected_cause=request.POST["suspected_cause"]
		immediate_actions_taken=request.POST["immediate_actions_taken"]
		sub_incident_types=request.POST["sub_incident_types"]
		reported_by=request.POST["reported_by"]

		information = Information.objects.create(
			location = location,
			incident_description = incident_description,
			date = date,
			time = time,
			incident_location = incident_location,
			initial_severity = initial_severity,
			suspected_cause = suspected_cause,
			immediate_actions_taken = immediate_actions_taken,
			sub_incident_types = sub_incident_types,
			reported_by = reported_by
			)
		print(information.incident_description)
		return render(request,"dashboard1.html",{"information":information})

def save_exit(request):
	logout(request)
	return redirect("/")

def view_all(request):
	information = Information.objects.all()
	print(information)
	return render(request,"view.html",{"information":information})


















