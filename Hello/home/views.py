from datetime import datetime
from django import db
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
# from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context ={
        "vartiable": "this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html',)
    # return HttpResponse("this is aboutpage")

def services(request):
    return render(request, 'service.html',)
    # return HttpResponse("this is services")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,)
        # contact.save()
    return render(request, 'contact.html',)
    # return HttpResponse("this is contact")
