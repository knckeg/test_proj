from django.contrib import admin
from .models import Team, Person, Stanowisko, Osoba

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

admin.site.register(Team, TeamAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'shirt_size', 'month_added', 'team')
    list_filter = ('shirt_size', 'month_added', 'team')
    search_fields = ('name',)

admin.site.register(Person, PersonAdmin)

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    list_filter = ('nazwa',)
    search_fields = ('nazwa',)

admin.site.register(Stanowisko, StanowiskoAdmin)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania')
    list_filter = ('stanowisko', 'data_dodania')
    search_fields = ('imie', 'nazwisko')
    readonly_fields = ('data_dodania',)
    ordering = ['nazwisko']

    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

admin.site.register(Osoba, OsobaAdmin)
