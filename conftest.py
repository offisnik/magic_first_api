import httpx as x
import pytest

# Получение нового Токена
@pytest.fixture(scope="session")
def get_token():
    response = x.post('https://aqa-proka4.org/sandbox/api/reset-token')
    my_token = response.json()['bearer_token']
    return my_token

