from django.urls import path
from . import views

urlpatterns = [
    #url mapping of register page
    path('register', views.register,name="register"),

    #url mapping of login page
    path('login', views.login,name="login"),

    #url mapping of logout page
    path('logout', views.logout,name="logout"),
   
]

