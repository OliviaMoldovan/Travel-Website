from django.db import models


class Customer(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nume = models.CharField(max_length=255, null=True)
    Prenume = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=255, null=True)
    PhoneNumber = models.CharField(max_length=12, null=True)
    Username = models.CharField(max_length=255, null=True)


class Airplane(models.Model):
    ID = models.IntegerField(primary_key=True)
    Agentie = models.CharField(max_length=255, null=True)
    Pornire = models.CharField(max_length=255, null=True)
    Destinatie = models.CharField(max_length=255, null=True)
    Pret = models.IntegerField()
    Data = models.DateField()


class Hotel(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nume = models.CharField(max_length=255, null=True)
    Locatie = models.CharField(max_length=255, null=True)
    Adresa = models.CharField(max_length=255, null=True)
    PretNoapte = models.IntegerField()
    img = models.ImageField(upload_to='pics')


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


class Book(models.Model):
    ID = models.IntegerField(primary_key=True)
    Destinatie = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Avion = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    DataInceperii = models.DateField()
    Durata = models.CharField(max_length=255, null=True)
    NrAdulti = models.IntegerField()
    NrCopii = models.IntegerField()
    Pret = models.IntegerField()
