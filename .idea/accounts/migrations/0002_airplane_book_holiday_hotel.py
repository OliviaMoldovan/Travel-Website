# Generated by Django 3.2.8 on 2021-11-30 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Agentie', models.CharField(max_length=255, null=True)),
                ('Destinatie', models.CharField(max_length=255, null=True)),
                ('Pret', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Nume', models.CharField(max_length=255, null=True)),
                ('Locatie', models.CharField(max_length=255, null=True)),
                ('Adresa', models.CharField(max_length=255, null=True)),
                ('PretNoapte', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Destinatie', models.CharField(max_length=255, null=True)),
                ('Pret', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('Avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.airplane')),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('DataInceperii', models.DateField()),
                ('Durata', models.CharField(max_length=255, null=True)),
                ('NrAdulti', models.IntegerField()),
                ('NrCopii', models.IntegerField()),
                ('Pret', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('Avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.airplane')),
                ('Destinatie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.holiday')),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hotel')),
            ],
        ),
    ]