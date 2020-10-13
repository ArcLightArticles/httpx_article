from typing import Dict

import fastapi

from .httpx_client import HTTPX_client

app = fastapi.FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


@app.get("/call")
async def http_call() -> Dict[str, str]:
    response = await call_something()
    if response.status_code == 200:
        return {"STATUS": "OK"}
    return {"STATUS": "ERROR"}


async def call_something():
    async with HTTPX_client.get_client() as client:
        return await client.get('https://httpbin.org/get')
