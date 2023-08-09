from django.urls import path
from .views import userlogin,usersignup,maindashboard,userlogout

urlpatterns = [
    path("login/",userlogin,name="login"),
    # path("logout/",userlogout,name="logout"),
    path("signup/",usersignup,name="signup"),
    path("main/",maindashboard,name="main"),
]
