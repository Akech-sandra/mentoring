from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from.models import *
from.forms import *

# Create your views here.
def index(request):
    return render(request, 'daycare_app/index.html')

def login(request):
    getloginform = Loginform()
    myuser = Loginform(request.POST)
    if request.method == 'POST':
        if myuser.is_valid():
            myuser.save
            return redirect('index')
        else:
            myuser = Login()    
    return render(request, 'daycare_app/login.html', {'getloginform': getloginform})



def signup(request):
    getsignupform = Signupform()
    myadmin = Signupform(request.POST)
    if request.method == 'POST':
        if myadmin.is_valid():
            myadmin.save
            return redirect('login')
        else:
            myadmin = Signup()    
    return render(request, 'daycare_app/signup.html', {'getsignupform': getsignupform})


