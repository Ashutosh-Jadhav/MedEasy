from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def Book(request):

    return render(request, 'Book.html')

def login(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('DoctorDetails')
        else:
            message.info(request, 'invalid email or password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def NewAccount(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('NewAccount')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email taken')
            return redirect('NewAccount')
        else:
            user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            user.save()
            user=auth.authenticate(username=username, password=password1)
            auth.login(request, user)
            return redirect('DoctorDetails')
    else:
        return render(request, 'NewAccount.html')