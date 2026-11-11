from django.contrib import admin
from .models import Gyarto, Model, Type, Car, Extras,Image

# Register your models here.
admin.site.register(Gyarto)
admin.site.register(Model)
admin.site.register(Type)
#admin.site.register(Car)
admin.site.register(Extras)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    max_num = 6
    validate_max = True

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [ImageInline]