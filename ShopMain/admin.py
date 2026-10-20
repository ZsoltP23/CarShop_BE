from django.contrib import admin
from .models import Gyarto, Model, Type, Car, Extras

# Register your models here.
admin.site.register(Gyarto)
admin.site.register(Model)
admin.site.register(Type)
admin.site.register(Car)
admin.site.register(Extras)