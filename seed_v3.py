import datetime
import os
import shutil
import sqlite3
import subprocess
import sys

BASE = r"C:\Users\zsoty\Documents\CarShop_BE"        # a projekt mappa (ahol a manage.py van)
SQL = r"C:\Users\zsoty\Downloads\autok_v3.sql"        # a letöltött SQL fájl
DB = os.path.join(BASE, "db.sqlite3")

ADMIN_USER, ADMIN_EMAIL, ADMIN_PASS = "admin", "admin@example.com", "Valtoztasd123!"


def manage(*args, env=None):
    print(">> python manage.py", *args)
    subprocess.run([sys.executable, "manage.py", *args], cwd=BASE, check=True, env=env)


if not os.path.exists(SQL):
    sys.exit(f"Nem találom az SQL fájlt: {SQL}")

# 1. a régi adatbázis mentése és törlése
if os.path.exists(DB):
    mentes = DB.replace(".sqlite3", f"_mentes_{datetime.datetime.now():%Y%m%d_%H%M%S}.sqlite3")
    shutil.copy(DB, mentes)
    os.remove(DB)
    print("Mentés:", mentes)

# 2. az összes tábla létrehozása (a Django alap táblái + a ShopMain táblák)
manage("makemigrations", "ShopMain")
manage("migrate")

# 3. feltöltés az autok_v3.sql adataival
con = sqlite3.connect(DB)
con.executescript(open(SQL, encoding="utf-8").read())
con.commit()
for tabla in ["ShopMain_gyarto", "ShopMain_model", "ShopMain_type", "ShopMain_car", "ShopMain_extras"]:
    print(f"{tabla}: {con.execute(f'SELECT COUNT(*) FROM {tabla}').fetchone()[0]} sor")
con.close()

# 4. admin felhasználó
env = dict(os.environ, DJANGO_SUPERUSER_PASSWORD=ADMIN_PASS)
manage("createsuperuser", "--noinput", "--username", ADMIN_USER, "--email", ADMIN_EMAIL, env=env)

print(f"Kész. Admin belépés: {ADMIN_USER} / {ADMIN_PASS}")