import asyncio
import aiohttp
import time
async def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
async def main():
    start_time = time.time()  
    tasks = [fetch_users() for _ in range(5)]
    responses = await asyncio.gather(*tasks)  
    users = responses[0]
    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]
    print("Names:", names)
    print("Emails:", emails)
    print("Usernames:", usernames)
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")
if __name__ == "__main__":
    asyncio.run(main())
