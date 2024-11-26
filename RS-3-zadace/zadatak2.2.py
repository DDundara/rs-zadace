import asyncio
async def fetch_users():
    print("Započinjem dohvaćanje korisničkih podataka...")
    await asyncio.sleep(3)  
    users = [
        {"id": 1, "ime": "Ana"},
        {"id": 2, "ime": "Ivan"},
        {"id": 3, "ime": "Marko"}
    ]
    print("Korisnički podaci dohvaćeni.")
    return users
async def fetch_products():
    print("Započinjem dohvaćanje podataka o proizvodima...")
    await asyncio.sleep(5) 
    products = [
        {"id": 101, "name": "Laptop", "cjena": 7500},
        {"id": 102, "name": "Mobitel", "cjena": 4500},
        {"id": 103, "name": "Slusalice", "cjena": 300}
    ]
    print("Podaci o proizvodima dohvaćeni.")
    return products
async def main():
    users, products = await asyncio.gather(fetch_users(), fetch_products())
    print("\nDohvaćeni korisnički podaci:", users)
    print("Dohvaćeni podaci o proizvodima:", products)
if __name__ == "__main__":
    asyncio.run(main())
