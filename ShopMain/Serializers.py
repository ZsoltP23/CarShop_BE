from .models import Gyarto, Model, Type, Car, Extras, Image
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


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
        read_only_fields = ['owner']

class SerExtras(ModelSerializer):
    class Meta:
        model = Extras
        fields = '__all__'

class SerImage(ModelSerializer):
    class Meta:
        model = Image
        fields = ["id","car","image"]

    def validate_car(self, car):
        if car.image.count() >= 6:
            raise serializers.ValidationError(
                f"Egy autóhoz max 6 kép"
            )
        return car

class SerHome(serializers.ModelSerializer):
    gyarto = serializers.CharField(source="gyarto_id.gyarto", read_only=True)
    model = serializers.CharField(source="model_Id.model", read_only=True)
    eng_volume = serializers.CharField(source="type_id.eng_volume", read_only=True)
    type = serializers.CharField(source="type_id.type", read_only=True)
    drive_method = serializers.IntegerField(source="type_id.drive_method", read_only=True)
    le = serializers.IntegerField(source="type_id.le", read_only=True)
    gearbox = serializers.IntegerField(source="type_id.gearbox", read_only=True)
    image = SerImage(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ["id", "gyarto", "model", "eng_volume", "type",
                  "drive_method", "le", "gearbox",
                  "colour", "registration_date", "price_eur","image"]


class SerDes(SerHome):

    extras = SerExtras(many=True, read_only=True)
    owner = serializers.CharField(source="owner.username", read_only=True, allow_null=True)

    upload_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False,
        max_length=6
    )
    images = SerImage(many=True, read_only=True)

    class Meta:
        model = Car
        fields = SerHome.Meta.fields + ["vin_code","template_plate","extras","owner","images","upload_images"]

    def create(self, validated_data):
        files = validated_data.pop("uploaded_images", [])
        car = super().create(validated_data)
        for f in files:
            Image.object.create(car=car, image=f)
        return car


User = get_user_model()

class SerRegister(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields = ['username','email','password','password2']

    def validate(self, attrs):
        if attrs["password"] == attrs["password2"]:
            attrs.pop("password2")
            return attrs
        else:
            raise serializers.ValidationError({"password2": "A két jelszó nem egyezik."})

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)