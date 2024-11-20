#Zadatak 4: Klase i objekti
import datetime
import math
from datetime import datetime
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina proizvodnje: {self.godina_proizvodnje}, Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")
auto = Automobil("Toyota", "Corolla", 2015, 120000)
auto.ispis()
auto.starost()
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b if self.b != 0 else "Nemoguće dijeliti s nulom"

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return self.a ** 0.5 if self.a >= 0 else "Nemoguće izračunati korijen od negativnog broja"
kalk = Kalkulator(4, 2)
print(kalk.zbroj())
print(kalk.oduzimanje())
print(kalk.mnozenje())
print(kalk.dijeljenje())
print(kalk.potenciranje())
print(kalk.korijen())
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]
najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime} s prosjekom ocjena {najbolji_student.prosjek():.2f}")
import math

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r ** 2
krug = Krug(5)
print(f"Opseg kruga: {krug.opseg():.2f}")
print(f"Površina kruga: {krug.povrsina():.2f}")
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Plaća radnika {radnik.ime} sada iznosi {radnik.placa}")
radnik = Radnik("Pero", "Programer", 6000)
manager = Manager("Ana", "Šef tima", 8000, "IT odjel")
radnik.work()
manager.work()
manager.give_raise(radnik, 500)
