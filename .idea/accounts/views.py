from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Holiday, Hotel, Airplane

from accounts.forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Contul a fost creat pentru  ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')
            if username and password:
                exists = User.objects.filter(username=username).exists()
                print(exists)
                if exists:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('home')
                else:
                    messages.info(request, 'Email-ul sau parola sunt incorecte!')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    holidays = Holiday.objects.all()
    hotels = Hotel.objects.all()
    airplanes = Airplane.objects.all()
    return render(request, 'index.html', {'holidays': holidays, 'hotels': hotels, 'airplanes': airplanes})


@login_required(login_url='login')
def myAccount(request):
    return render(request, 'myaccount.html')
