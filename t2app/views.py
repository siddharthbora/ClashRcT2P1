from django.shortcuts import render
from django.http import HttpResponse
from .models import Sid

# Create your views here.


def reg(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        gender = request.POST['gender']
        a=Sid.objects.filter(Name=fname+' '+lname)
        b=Sid.objects.filter(email=email)
        if a | b:
            return render(request,"tem/userfound.html",{'msg':["user name already exist"]})
        x = Sid(Name=fname + ' ' + lname, email=email, phoneNo=phoneno, gender=gender)
        x.save()
        return render(request, 'tem/userfound.html', {'msg': ["User Added Successfully"]})
    return render(request, 'tem/home.html')


def search(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Sid.objects.filter(email=email)
        if not user:
            return render(request, 'tem/userfound.html', {'msg': ["Sorry No User Found"]})
        return render(request, 'tem/userfound.html', {'data': user, 'msg': ['User Found']})
    return render(request,'tem/search.html')
