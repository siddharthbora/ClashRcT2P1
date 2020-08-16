from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

def login(request):
    form=UserChangeForm()
    return render(request,'tem/login.html',{'form':form})