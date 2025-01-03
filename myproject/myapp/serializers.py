from rest_framework import serializers

from myapp.models import Team, Stanowisko, Osoba

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)
    plec = serializers.ChoiceField(choices=[
        (1, 'Kobieta'),
        (2, 'Mężczyzna'),
        (3, 'Inna'),
    ])
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all(), required=False)

    def create(self, validated_data):
        """
        Tworzy nowy obiekt Osoba na podstawie danych wejściowych.
        """
        stanowisko = validated_data.get('stanowisko')
        osoba = Osoba.objects.create(**validated_data)
        osoba.stanowisko = stanowisko
        osoba.save()
        return osoba

    def update(self, instance, validated_data):
        """
        Aktualizuje istniejący obiekt Osoba na podstawie danych wejściowych.
        """
        stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = stanowisko
        instance.save()
        return instance

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country']

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']

class OsobaModelSerializer(serializers.ModelSerializer):
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko']