#Zadatak 1: Lambda izrazi
#zadatak 1.1
kvadriraj = lambda x: x ** 2
print(kvadriraj(5))

#zadatak 1.2
zbroji_pa_kvadriraj = lambda a, b: (a + b) ** 2
print(zbroji_pa_kvadriraj(1, 3))

#zadatak 1.3
kvadriraj_duljinu = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu([2, 3, 4, 5]))

#zadatak 1.4
pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x
print(pomnozi_i_potenciraj(4, 5))

#zadatak 1.5
paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(3))
print(paran_broj(8))

