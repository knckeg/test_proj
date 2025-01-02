from django.contrib import admin
from .models import Team, Person, Stanowisko, Osoba

# Register the Team model
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

admin.site.register(Team, TeamAdmin)

# Register the Person model
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'shirt_size', 'month_added', 'team')
    list_filter = ('shirt_size', 'month_added', 'team')
    search_fields = ('name',)

admin.site.register(Person, PersonAdmin)

# Register the Stanowisko model
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    search_fields = ('nazwa',)

admin.site.register(Stanowisko, StanowiskoAdmin)

# Register the Osoba model
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania')
    list_filter = ('plec', 'stanowisko')
    search_fields = ('imie', 'nazwisko')
    readonly_fields = ('data_dodania',)

# Ensure Osoba is registered only once
admin.site.register(Osoba, OsobaAdmin)
