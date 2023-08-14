from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .serializers import SignUpFormSerializer,LoginFormSerializer


# Create your views here.
def userlogin(request):
    if request.method == "POST":
        serializer = LoginFormSerializer(data = request.POST)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username,password=password)
            login(request,user)
            if user is not None:
                return redirect('main')
            else:
                return render(request, "login.html", {"error": "Either username or password is wrong."})
        else:
            # Handle validation errors
            error_messages = serializer.errors  # Dictionary of field-specific error messages
            return render(request, "login.html", {"errors": error_messages})
    else:
        return render(request, "login.html",{})


def usersignup(request):
    if request.method == "POST":
        serializer = SignUpFormSerializer(data=request.POST)
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.set_password(serializer.validated_data["password"])
                user.save()
                return redirect('login')
        except Exception as e:
            error_messages = str(e)
            return error_messages
    else:
        return render(request, "signup.html", {})


def maindashboard(request):
    return render(request, "main.html")


def userlogout(request):
    return redirect("login/")
