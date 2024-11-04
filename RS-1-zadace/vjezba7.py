def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        return "Lozinka mora sadržavati između 8 i 15 znakova"
    sadrzi_veliko_slovo = any(char.isupper() for char in lozinka)
    sadrzi_broj = any(char.isdigit() for char in lozinka)
    
    if not sadrzi_veliko_slovo or not sadrzi_broj:
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    return "Lozinka je jaka!"
while True:
    lozinka = input("Unesite lozinku: ")
    poruka = provjera_lozinke(lozinka)
    print(poruka) 
    if poruka == "Lozinka je jaka!":
        break  