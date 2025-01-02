from django.contrib import admin

from .models import Team, Person

from .models import Osoba, Stanowisko

admin.site.register(Team)
admin.site.register(Person)

@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    search_fields = ('nazwa',)

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko')
    readonly_fields = ('data_dodania',)
    list_filter = ('plec', 'stanowisko')
    search_fields = ('imie', 'nazwisko')

admin.site.register(Osoba, OsobaAdmin)