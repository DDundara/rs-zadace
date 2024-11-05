def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    broj_samoglasnika = 0
    broj_suglasnika = 0
    for znak in tekst:
        if znak in vowels:
            broj_samoglasnika += 1
        elif znak in consonants:
            broj_suglasnika += 1
    rezultat = {
        'vowels': broj_samoglasnika,
        'consonants': broj_suglasnika
    }
    return rezultat
tekst = "Python je jednostavan i moćan programski jezik koji se koristi u raznim područjima poput web razvoja, znanosti o podacima."
print(count_vowels_consonants(tekst)) 
