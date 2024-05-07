from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from HomePage.models import *

# Create your views her

authenticated = False


def admin_login(request):
    global authenticated
    if authenticated:
        return redirect('/comments/')
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        print(username,password)

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Username doesn't exists")
            return redirect('/author/')

        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/author/')
        else:
            authenticated = True
            login(request,user)
            return redirect('/comments/')

    return render(request,"login_page.html")


def show_comment(request):
    global authenticated
    if authenticated:
        comments = Reviewer.objects.all()
        return render(request,"comments.html",context={'comments':comments})
    else:
        return redirect('/author/')


def delete_comment(request,id):
    global authenticated
    if authenticated:
        Reviewer.objects.filter(id=id).delete()
    return redirect('/comments/')


def admin_logout(request):
    global authenticated
    authenticated = False
    logout(request)
    return redirect('/author/')