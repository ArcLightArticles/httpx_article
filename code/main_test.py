import httpx
import pytest
import fastapi.testclient

from . import main


@pytest.fixture
def api():
    return fastapi.testclient.TestClient(main.app)


@pytest.fixture
def async_api():
    return httpx.AsyncClient(app=main.app, base_url="http://test")


def test_hello(api):
    response = api.get('/')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"Hello": "World"}


@pytest.mark.asyncio
async def test_http(async_api):
    await async_api.get('/call')
    await async_api.get('/call')
    response = await async_api.get('/call')
    response.raise_for_status()
    response_json = response.json()
    assert response_json == {"STATUS": "OK"}
