import asyncio
import random
import time
import aiohttp

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://python.org"
]

async def fetch_url(url):
    print(f"[{time.ctime()}] Fetching {url}...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
            print(f"[{time.ctime()}] Done {url} {len(text)} bytes.")
            return url, len(text)

async def main():
    random_urls = random.sample(urls, len(urls))

    print("Random Order: ", random_urls)

    tasks = [asyncio.create_task(fetch_url(url)) for url in random_urls]
    results = await asyncio.gather(*tasks)
    print("results:", results   )

asyncio.run(main())
