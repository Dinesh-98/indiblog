from django.shortcuts import render
from django.contrib import messages
from .models import AppModel
# Create your views here.

def home(request):
    obj=AppModel.objects.all()
    return render(request,"home.html",{'obj':obj})

def login(request):
     if request.method=="POST":
          username=request.POST["username"]
          password=request.POST["password"]

          user=auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user)
               return redirect("/")
          else:
               message.error("Invalid credentials")     