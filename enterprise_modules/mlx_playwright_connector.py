import asyncio
from playwright.async_api import async_playwright

async def launch_stealth_browser(proxy: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            proxy={
                'server': f'http://{proxy}'
            }
        )
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://api.ipify.org')
        ip = await page.text_content('body')
        print(f"Browser IP via proxy: {ip}")
        await browser.close()

if __name__ == "__main__":
    # Example usage
    proxy = "user:pass@1.2.3.4:1080"
    asyncio.run(launch_stealth_browser(proxy))
