"""Fetch a web page via Zyte API and print the HTML."""
import os, sys, asyncio
from zyte_api import AsyncZyteAPI

async def fetch(url):
    with open(os.path.join(os.path.dirname(__file__), '..', '..', '.env')) as f:
        for line in f:
            if line.startswith('ZYTE_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
    client = AsyncZyteAPI(api_key=api_key)
    result = await client.get({'url': url, 'browserHtml': True})
    print(result.get('browserHtml', ''))

if __name__ == '__main__':
    asyncio.run(fetch(sys.argv[1]))
