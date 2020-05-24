from django.http import HttpResponse
from django.shortcuts import render
from .models import Register

def index(requests):

    return render(requests, "hrapp/index.html")
    #return HttpResponse("Index Page")


def about(requests):
    #return HttpResponse("Welcome to About page")
    return render(requests, "hrapp/about.html")


def services(requests):
	if requests.method=="POST":
		obj = Register(emailID = requests.POST["txtemail"],password=requests.POST["txtpass"],mobile=requests.POST["txtmobile"],Fullname=requests.POST["txtfname"],address=requests.POST["txtaddress"])
		obj.save()
		return render(requests, "hrapp/services.html", {"msg":"You have Registered Succesfully"}) 
	return render(requests, "hrapp/services.html")

def contact(requests):
    return render(requests, "hrapp/contact.html")


def gallery(requests):
    return render(requests, "hrapp/gallery.html")