class Narudzba:
    def __init__(self, proizvodi):
        self.proizvodi = proizvodi
        self.ukupna_cijena = sum([proizvod["cijena"] * proizvod["kolicina"] for proizvod in proizvodi])

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join([f"{proizvod['naziv']} x {proizvod['kolicina']}" for proizvod in self.proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} EUR")

# Funkcija koja vraća novu narudžbu
def napravi_narudzbu(proizvodi):
    if not isinstance(proizvodi, list) or not proizvodi:
        raise ValueError("Proizvodi moraju biti lista i ne mogu biti prazna.")
    for proizvod in proizvodi:
        if not isinstance(proizvod, dict) or not all(k in proizvod for k in ["naziv", "cijena", "kolicina"]):
            raise ValueError("Svaki proizvod mora biti rječnik s ključevima 'naziv', 'cijena' i 'kolicina'.")
        if proizvod["kolicina"] <= 0:
            raise ValueError(f"Proizvod {proizvod['naziv']} nema dostupnu količinu.")
    return Narudzba(proizvodi)
