from django.core.validators import MinLengthValidator,RegexValidator
from django.conf import settings

from django.db import models

class Gyarto(models.Model):

    gyarto = models.CharField(max_length=50)
    orszag = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.gyarto}"

class Model(models.Model):

    gyarto_Id = models.ForeignKey(Gyarto, on_delete=models.CASCADE, related_name="modellek")
    model = models.CharField(max_length=255)
    yrs_from = models.DateTimeField()
    yrs_til = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.model}' 

class Type(models.Model):

    model_Id = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='Tipusa')
    eng_volume = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    drive_method = models.IntegerField(max_length=255)
    le = models.IntegerField()
    gearbox = models.IntegerField(max_length=255)

    def __str__(self):
        return f'{self.type}'

class Extras(models.Model):

    extra = models.CharField(default=255)
    extras = models.ManyToManyField("self")


class Car(models.Model):

    gyarto_id = models.ForeignKey(Gyarto, on_delete=models.CASCADE, related_name='gyarto_id')
    model_Id = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='modell_id')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_id')
    extras = models.ManyToManyField(Extras, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True,
                              related_name='cars')

    vin_code = models.CharField(
        max_length=17,
        unique=True,
        validators=[
            MinLengthValidator(17),
            RegexValidator(r"^[A-HJ-NPR-Z0-9]{17}$")
        ])
    template_plate = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            MinLengthValidator(8),
            RegexValidator("^[A-Z]{4}-\d{3}$")
        ]
    )
    colour = models.CharField(default=255)
    prd_yr = models.IntegerField()
    registration_date = models.DateTimeField()
    mileages_km = models.IntegerField()
    price_eur = models.IntegerField()
    notes = models.CharField(default=255)

class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images",null=True, blank=True)
    image = models.ImageField(upload_to="static/%Y/%m/")

    def clean(self):
        super().clean()
        if self.car_id:
            existing = Image.objects.filter(car_id=self.car_id).exclude(pk=self.pk).count()
            if existing >= 6:
                raise (
                    f"Egy autóhoz maximum 6 kép tölthető fel"
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)