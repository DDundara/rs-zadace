import asyncio
baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
async def autorizacija(korisnik, unesena_lozinka):
    print(f"Pokrećem autorizaciju za korisnika: {korisnik['korisnicko_ime']}...")
    await asyncio.sleep(2)  
    baza_podaci = next((item for item in baza_lozinka if item['korisnicko_ime'] == korisnik['korisnicko_ime']), None)
    if baza_podaci and baza_podaci['lozinka'] == unesena_lozinka:
        return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
    return f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."
async def autentifikacija(korisnik):
    print(f"Pokrećem autentifikaciju za korisnika: {korisnik['korisnicko_ime']}...")
    await asyncio.sleep(3) 
    korisnik_iz_baze = next(
        (item for item in baza_korisnika if item['korisnicko_ime'] == korisnik['korisnicko_ime'] and item['email'] == korisnik['email']),
        None
    )
    if not korisnik_iz_baze:
        return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."
    rezultat_autorizacije = await autorizacija(korisnik_iz_baze, korisnik['lozinka'])
    return rezultat_autorizacije
async def main():
    uneseni_korisnik = {
        'korisnicko_ime': 'ana_anic',
        'email': 'aanic@gmail.com',
        'lozinka': 'super_teska_lozinka'
    }
    rezultat = await autentifikacija(uneseni_korisnik)
    print(rezultat)
if __name__ == "__main__":
    asyncio.run(main())
