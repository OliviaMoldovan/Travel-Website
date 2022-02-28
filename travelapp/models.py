from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True)
    photo = models.ImageField(upload_to='pics')
    review = models.CharField(max_length=5000, default='Review')

class Airplane(models.Model):
    ID = models.IntegerField(primary_key=True)
    Agentie = models.CharField(max_length=255, null=True)
    Pornire = models.CharField(max_length=255, null=True)
    Destinatie = models.CharField(max_length=255, null=True)
    Pret = models.IntegerField()


class Hotel(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nume = models.CharField(max_length=255, null=True)
    Locatie = models.CharField(max_length=255, null=True)
    Adresa = models.CharField(max_length=255, null=True)
    PretNoapte = models.IntegerField()

class Holiday(models.Model):
    ID = models.IntegerField(primary_key=True)
    Destinatie = models.CharField(max_length=255, null=True)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Avion = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    Pret = models.IntegerField()
    Data = models.DateField()
    Durata = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    NrAdulti = models.IntegerField()
    Descriere = models.CharField(max_length=10000)


class Book(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    DataInceperii = models.DateField()
    Durata = models.CharField(max_length=255, null=True)
    NrAdulti = models.IntegerField()
    NrCopii = models.IntegerField()
    Pret = models.IntegerField()
    Avion_id = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    Hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Destinatie = models.CharField(max_length=255, null=False)





