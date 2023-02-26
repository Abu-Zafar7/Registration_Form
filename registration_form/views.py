from django.shortcuts import redirect, render
from django.http import HttpResponse
from registration_form.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def homepage(request):
    return render(request,'registration_form/homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account created for {username}!")
            return redirect('homepage')
            

    else:
        form = SignUpForm()
    return render(request,"registration_form/signup.html",{"form": form})   

def loginuser(request):
    
        context = {}
        if request.method == 'POST':
            

            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username = username, password = password)

            if user is not None:
                login(request,user)
                messages.success(request,f"Welcome {user}!")
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password") 
                
                
        else:
            return render(request,'registration_form/homepage.html',context)
        return render(request,'registration_form/homepage.html',context)   

def logoutuser(request):
    logout(request)
    return redirect('homepage')


    