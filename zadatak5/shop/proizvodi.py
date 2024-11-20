class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"{self.naziv}: {self.cijena} EUR, Količina: {self.kolicina}")

# Lista proizvoda
proizvodi = []

# Funkcija za dodavanje proizvoda u listu
def dodaj_proizvod(proizvod_data):
    proizvod = Proizvod(proizvod_data["naziv"], proizvod_data["cijena"], proizvod_data["kolicina"])
    proizvodi.append(proizvod)
