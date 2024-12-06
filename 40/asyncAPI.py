#40. Implementera en funktion som laddar data asynkront från en API.

import aiohttp
import asyncio

async def fetch_data(session, url):
    """
    Hämtar data från en API-endpoint asynkront.
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Kontrollera om det blev några fel
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Fel vid hämtning från {url}: {e}")
        return None

async def fetch_multiple(urls):
    """
    Hämtar data från flera API-endpoints parallellt.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    # Exempel-API-URL: Byt ut med riktiga API-endpoints
    api_urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    # Kör asynkron funktionalitet
    results = asyncio.run(fetch_multiple(api_urls))
    for i, result in enumerate(results):
        print(f"Resultat för URL {i+1}: {result}")
