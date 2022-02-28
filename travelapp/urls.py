from django.urls import path
from . import views

urlpatterns = [
   path('', views.homePage, name='home'),
   path('home', views.homePage, name='home'),
     path('login', views.loginPage, name='login'),
   path('logout', views.logoutUser, name="logout"),
   path('myaccount', views.myAccount, name='myaccount'),

]
