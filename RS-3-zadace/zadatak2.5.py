import asyncio
async def secure_data(podaci):
    print(f"Pokrećem enkripciju za prezime: {podaci['prezime']}...")
    await asyncio.sleep(3)  
    return {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }
async def main():
    osjetljivi_podaci = [
        {'prezime': 'Horvat', 'broj_kartice': '1234567812345678', 'CVV': '123'},
        {'prezime': 'Kovačić', 'broj_kartice': '9876543298765432', 'CVV': '456'},
        {'prezime': 'Novak', 'broj_kartice': '1111222233334444', 'CVV': '789'}
    ]
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)
if __name__ == "__main__":
    asyncio.run(main())
