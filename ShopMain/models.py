from django.db import models

class Gyarto(models.Model):

    marka = models.CharField(max_length=50)
    Orszag = models.CharField(max_length=50, blank=True, null=True)
    Marka_Logo = models.ImageField(upload_to="static/images/Marka_logo")

    def __str__(self):
        return f"{self.marka}" #{self.Marka_Logo}

class Modell(models.Model):

    marka = models.ForeignKey(Gyarto, on_delete=models.CASCADE, related_name="modellek")
    Modell_nev = models.CharField(max_length=255)
    evjarat = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.marka},{self.Modell_nev}' 

class Tipus(models.Model):

    modell = models.ForeignKey(Modell, on_delete=models.CASCADE, related_name='Tipusa')
    #VetelAra = models.DecimalField(default=0, max_digits=10)
    VetalAra = models.IntegerField(default=67)
    kmOra = models.IntegerField(default=0, null=True, blank=True)

    UZEMANYAG = ((1,"Benzin"),(2,"Dízel"),(3,"Hybrid"),(4,"Elektromos"))
    uzemanyag = models.IntegerField( choices=UZEMANYAG )

    KIVITEL = ((1,"Sedan"),(2,"Kombi"),(3,"Coupe"),(4,"Cabrio"),(5,"Hatchback"),(5,"Tank"))
    kivitel = models.IntegerField( choices=KIVITEL )

    ALLAPOT = ((1,"Használt"),(2,"Új"),(3,"Veterán"))
    Allapot = models.IntegerField(choices=ALLAPOT)

    Hengerurtartalom = models.IntegerField(null=True, blank=True)

    Ajtok_szama = models.IntegerField(null=True,)

    Automata = models.BooleanField(default=False,null=True)
    Osszkerekes = models.BooleanField(default=False,null=True)
    Klima = models.BooleanField(default=True,null=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)