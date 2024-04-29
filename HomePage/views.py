from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        feedback = data.get('feedback')
        obj = Reviewer(name=name,email=email,feedback=feedback)
        obj.save()
        messages.info(request,"Thanks for your feedback")
        return redirect('/')
    return render(request,"TEST.html")