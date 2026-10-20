from .models import Gyarto, Model, Type, Car, Extras
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class SerGyarto(ModelSerializer):
    class Meta:
        model = Gyarto
        fields = '__all__'

class SerModel(ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class SerType(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class SerCar(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class SerExtras(ModelSerializer):
    class Meta:
        model = Extras
        fields = '__all__'

class SerHome(serializers.ModelSerializer):
    gyarto = serializers.CharField(source="gyarto_id.gyarto", read_only=True)
    model = serializers.CharField(source="model_Id.model", read_only=True)
    eng_volume = serializers.CharField(source="type_id.eng_volume", read_only=True)
    type = serializers.CharField(source="type_id.type", read_only=True)
    drive_method = serializers.IntegerField(source="type_id.drive_method", read_only=True)
    le = serializers.IntegerField(source="type_id.le", read_only=True)
    gearbox = serializers.IntegerField(source="type_id.gearbox", read_only=True)

    class Meta:
        model = Car
        fields = ["id", "gyarto", "model", "eng_volume", "type",
                  "drive_method", "le", "gearbox",
                  "colour", "registration_date", "price_eur"]


class SerDes(SerHome):

    extras = SerExtras(many=True, read_only=True)

    class Meta:
        model = Car
        fields = SerHome.Meta.fields + ["vin_code","template_plate","extras"]