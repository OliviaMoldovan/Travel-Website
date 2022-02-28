import datetime
from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .booking import BookCommand, Receiver, Invoker
from .models import Holiday, Hotel, Airplane, User, Book
from .strategyInterface import *


def registerPage(request):
    User = get_user_model()
    if request.method == 'POST':
        first_name = request.POST['prenume']
        last_name = request.POST['nume']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username-ul a fost deja folosit')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Emailul a fost deja folosit')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                last_name=last_name,
                                                first_name=first_name, phone_number=phone)
                user.save()
                messages.info(request, 'Utilizatorul a fost creat cu succes! ')
                return redirect('login')
        else:
            messages.info(request, 'Ati introdus gresit parola ')
            return redirect('register')
    else:
        return render(request, 'register.html')


def loginPage(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            if username and password:
                exists = User.objects.filter(username=username).exists()
                if exists:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('home')
                else:
                    messages.info(request, 'Username-ul sau parola sunt incorecte!')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    message = ''
    user1 = request.user
    holidays = Holiday.objects.all()
    hotels = Hotel.objects.all()
    airplanes = Airplane.objects.all()
    user = User.objects.all()
    app = Context()
    if request.method == 'POST':
        if 'Rezerva1' in request.POST:
            Client_id = user1.id
            DataInceperii = request.POST['date']
            Data = datetime.date(int(DataInceperii[6:10]), int(DataInceperii[0:2]), int(DataInceperii[3:5]))
            strategy = request.POST['strategy']
            NrAdulti = int(request.POST['nr_adulti'])
            NrCopii = int(request.POST['nr_copii'])
            if strategy == "hotelS":
                Hotel_id = request.POST['Hotel']
                hotel = Hotel.objects.get(ID=Hotel_id)
                Durata = int(request.POST['Durata'])
                app.setStrategy(HotelStrategy(hotel.PretNoapte, Durata))
                pret_rezultat = app.executeStrategy()
                book = Book(DataInceperii=Data, Durata=Durata, NrAdulti=NrAdulti, NrCopii=NrCopii,
                            Pret=pret_rezultat, Avion_id =Airplane.objects.get(ID=0), Hotel_id=hotel, Client_id=user1,
                            Destinatie=hotel.Locatie)
            elif strategy == "avionS":
                Avion_id = request.POST['Destinatie']
                avion = Airplane.objects.get(ID=Avion_id)
                app.setStrategy(AirplaneStrategy(avion.Pret, NrAdulti, NrCopii))
                pret_rezultat = app.executeStrategy()
                book = Book(DataInceperii=Data, Durata=0, NrAdulti=NrAdulti, NrCopii=NrCopii,
                            Pret=pret_rezultat, Avion_id=avion, Hotel_id=Hotel.objects.get(ID=0), Client_id=user1,
                            Destinatie=avion.Destinatie)
            else:
                Hotel_id = request.POST['Hotel']
                Avion_id = request.POST['Destinatie']
                Durata = int(request.POST['Durata'])
                hotel = Hotel.objects.get(ID=Hotel_id)
                avion = Airplane.objects.get(ID=Avion_id)
                app.setStrategy(Default(hotel.PretNoapte, Durata, avion.Pret, NrAdulti, NrCopii))
                pret_rezultat = app.executeStrategy()
                book = Book(DataInceperii=Data, Durata=Durata, NrAdulti=NrAdulti, NrCopii=NrCopii,
                            Pret=pret_rezultat, Avion_id=avion, Hotel_id=hotel, Client_id=user1,
                            Destinatie=avion.Destinatie)
            book.save()
            message = "{} de {} €".format("Comanda dumneavoastra s-a inregistrat cu succes! Pretul "
                                          "final este ",
                                          pret_rezultat)
        if 'Rezerva' in request.POST:
            holiday = request.POST['Rezerva']
            RECEIVER = Receiver(holiday, user1)
            BOOKCOMMAND = BookCommand(RECEIVER)
            INVOKER = Invoker()
            INVOKER.register("1", BOOKCOMMAND)
            INVOKER.execute("1")
            message = "Calatorie placuta!"
    context = {'holidays': holidays, 'hotels': hotels, 'airplanes': airplanes, 'user': user,
               'user1': user1, 'message': message}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def myAccount(request):
    User1 = request.user
    message = ""
    if request.method == 'POST':
        review = request.POST.get('testimonial')
        if review:
            User1.review = review
            User1.save()
            message = "Opinia ta conteaza :)"
    context = {'message': message}
    return render(request, 'myaccount.html', context)
