import asyncio
async def fetch_data():
    print("Započinjem dohvaćanje podataka...")
    await asyncio.sleep(3)  
    data = [x for x in range(1, 11)]  
    print("Podaci dohvaćeni.")
    return data
async def main():
    data = await fetch_data()  
    print("Dohvaćeni podaci:", data)
if __name__ == "__main__":
    asyncio.run(main())