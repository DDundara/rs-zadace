from shop.proizvodi import dodaj_proizvod, proizvodi
from shop.narudzbe import napravi_narudzbu

# Dodajte proizvode u listu
proizvodi_data = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

# Dodajte svaki proizvod
for proizvod in proizvodi_data:
    dodaj_proizvod(proizvod)  # Dodajte proizvod u listu proizvodi

# Ispis proizvoda
for proizvod in proizvodi:
    proizvod.ispis()

# Kreiranje narudžbe
narudzba = napravi_narudzbu(proizvodi_data)
narudzba.ispis_narudzbe()
