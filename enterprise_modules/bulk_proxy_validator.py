import asyncio
import aiohttp
from typing import List

async def check_proxy(session, proxy):
    try:
        async with session.get('https://api.ipify.org', proxy=f'http://{proxy}', timeout=8) as resp:
            if resp.status == 200:
                ip = await resp.text()
                print(f"[VALID] {proxy} -> {ip}")
                return proxy, True
    except Exception as e:
        print(f"[INVALID] {proxy} | {e}")
    return proxy, False

async def validate_proxies(proxy_list: List[str], concurrency: int = 100):
    connector = aiohttp.TCPConnector(limit=concurrency)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [check_proxy(session, proxy) for proxy in proxy_list]
        results = await asyncio.gather(*tasks)
    valid = [proxy for proxy, ok in results if ok]
    invalid = [proxy for proxy, ok in results if not ok]
    print(f"\nSummary: {len(valid)} valid, {len(invalid)} invalid.")
    return valid, invalid

if __name__ == "__main__":
    # Example usage
    proxies = [
        "user:pass@1.2.3.4:1080",
        "user:pass@5.6.7.8:1080",
        # ...add up to 100+ proxies here
    ]
    asyncio.run(validate_proxies(proxies))
