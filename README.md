Admin belépés: admin / Valtoztasd123!
Teszt felhasználó: teszt / qwertzu8

#Szerver indítási adatok beírása

adatbázis fel lett töltve és be lett importálva az adatok

modelek:
- Gyarto: Marka és az ország van bennük pl: suzuki
- Model: Kifejezett modellek vannak bennük, pl: swift
- Type: Felszereltségre és motorváltozatra szűkít 
    pl: 1.3 GL
- Car: egy konkrét meghirdetett autó van benne. 
    Ami tartalmazza a 
    (gyarto,model,type,extras,user, információt is)
- Extras: felsorolt extrák vannak bennük
    pl: tempomat, üllésfűtés, önvezetés
- User: felhasználókat tartalmazza | a django alapértelmezett modelje
- Image: képeket tárol.

Gyarto->Model->Type->Car<-Extras
               User->Car<-Admin
               Images<-Car


View/URLs:

- home/ | ami
    "id", "gyarto", "model", "eng_volume", "type",
    "drive_method", "le", "gearbox",
    "colour", "registration_date", "price_eur"
    adatokat add vissza.
    CSAK "GET"
- des/ | ami a home-ot +
    "vin_code","template_plate","extras" +
    extrákat, ami egy másik adatbázisból jön!
    csak "GET","POST"
- des/id | ami a des-t id alapján keresi
    ugyan azok az adatok vannak benne, mint a des-ben
    csak "GET","PUT","DELETE"
- auth/login | belépés
- auth/refresh | új token hívása
- auth/register | új felhasználó létrehozása


+ az admin mindent tud csinálni. PUT,POST,DELETE
+ Az AI a gemini lesz 15 kérdés percenként. A kereső mezőnél lesz. Ami segyítheti a megfelelő autó kiválasztását. Pl.: "legyen kék, pici, városi autó, ami megbízhatónak számít." és kilistázza az ehhez legközelebb eső autókat az adatbázisból.
+ modellek és gyártók listázásas szűrőkkel.


POST:

{
    "id": 483,
    "gyarto": "Toyota",
    "model": "3-as sorozat",
    "eng_volume": "2.5",
    "type": "Hybrid Executive AWD-i",
    "drive_method": 3,
    "le": 222,
    "gearbox": 2,
    "colour": "255",
    "registration_date": "2026-11-11T10:09:49Z",
    "price_eur": 200,
    "vin_code": "SALLAAA128A593710",
    "template_plate": "RVJF-598",
    "extras": [
        {
            "id": 1,
            "extra": "Tolatókamera",
            "extras": []
        }
    ],
    "owner": "teszt",
    "images": [
        {
            "id": 1,
            "car": 483,
            "image": "/static/2026/11/wp7960363.jpg"
        }
    ]
}
