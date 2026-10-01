from .models import Gyarto, Modell, Tipus
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class SerGyarto(ModelSerializer):
    class Meta:
        model = Gyarto
        fields = '__all__'

class SerModell(ModelSerializer):
    class Meta:
        model = Modell
        fields = '__all__'

class SerTipus(ModelSerializer):
    class Meta:
        model = Tipus
        fields = '__all__'

class TeljesSer(ModelSerializer):
    gyarto = serializers.CharField(source="Gyarto.nev")
    gyarto_logo = serializers.CharField(source="Gyarto.Marka_Logo")
    model_neve = serializers.CharField(source="Modell_nev")

    class Meta:
        model = Tipus
        fields = ["id","gyarto","gyarto_logo","modell_neve","uzemanyag","kivitel",
                 "Ajtok_szama","updated"]
