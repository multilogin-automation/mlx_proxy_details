import argparse
import yaml
import sys
from enterprise_modules.bulk_proxy_validator import validate_proxies
from enterprise_modules.mlx_playwright_connector import launch_stealth_browser

CONFIG_PATH = 'config.yaml'

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description='Enhanced Multilogin X Proxy Toolbox')
    parser.add_argument('--bulk-validate', action='store_true', help='Bulk validate proxies')
    parser.add_argument('--playwright', metavar='PROXY', help='Launch Playwright browser with proxy')
    args = parser.parse_args()
    config = load_config()

    if args.bulk_validate:
        proxies = config.get('proxy_list', [])
        concurrency = config.get('concurrency', 100)
        import asyncio
        asyncio.run(validate_proxies(proxies, concurrency=concurrency))
    elif args.playwright:
        import asyncio
        asyncio.run(launch_stealth_browser(args.playwright))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
