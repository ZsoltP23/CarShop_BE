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

Gyarto->Model->Type->Car<-Extras
               User->Car->Admin

View/URLs:

jelenleg 2 van:
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

Felhasználók folyamatban!
+ egy admin felület, akinek mindent -kilistáz, -törölni tud, -mindenkihez hozzá is tud adni
+ AI implemetálása, pl egy autóról általános tudniválókat ír le, gyakori hibája, jellegzetessége, mire használják...
+ egy fő felhasználó, ami hozzá tud adni autókat 

POST:
{
  "type": 1,
  "extras": [3, 5],
  "vin_code": "JTD6XPV42T2RACKDA",
  "license_plate": "XLGJ-393",
  "colour": "zöld",
  "prd_yr": 2014,
  "registration_date": "2014-06-17",
  "mileages_km": 120000,
  "price_eur": 3900,
  "notes": ""
}
