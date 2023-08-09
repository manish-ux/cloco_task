from django.shortcuts import render,redirect

# Create your views here.
def userlogin(request):
    return render(request,'login.html')

def usersignup(request):
    return render(request,'signup.html')

def maindashboard(request):
    return render(request,'main.html')

def userlogout(request):
    return redirect('login/')