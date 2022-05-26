from django.shortcuts import redirect, render
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from chats import views as chat_views


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

class SignupView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request, 'core/signup.html', {'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Success !")
            return redirect('/signup')
        else:
            return render(request, 'core/signup.html', {'form':fm})


class MyLoginView(View):
    def get(self, request):
        fm = MyLoginForm()
        return render(request, 'core/login.html', {'form':fm})


    def post(self,request):
        fm = MyLoginForm(request, data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'core/login.html', {'form':fm})


        else:
            
         
            return render(request, 'core/login.html', {'form':fm})
            

    def chats(request):
        return render(request,'chats/home.html')
    
