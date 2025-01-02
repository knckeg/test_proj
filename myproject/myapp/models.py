from django.db import models


MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, null=False, blank=False)
    opis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        KOBIETA = 1, 'Kobieta'
        MEZCZYZNA = 2, 'Mężczyzna'
        INNA = 3, 'Inna'

    data_dodania = models.DateField(auto_now_add=True)

    imie = models.CharField(max_length=50, null=False, blank=False)
    nazwisko = models.CharField(max_length=50, null=False, blank=False)
    plec = models.IntegerField(choices=Plec.choices, null=False, blank=False)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE, related_name='osoby')

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ['nazwisko']