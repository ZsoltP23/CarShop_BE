Admin belépés: admin / Valtoztasd123!

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
- User: felhasználókat tartalmazza

View/URLs:

jelenleg 2 van:
- home/ ami 
    "id", "gyarto", "model", "eng_volume", "type",
    "drive_method", "le", "gearbox",
    "colour", "registration_date", "price_eur"
    adatokat add vissza.
- des / ami a home-ot +
    "vin_code","template_plate","extras" +
    extrákat, ami egy másik adatbázisból jön!

Felhasználók folyamatban!

