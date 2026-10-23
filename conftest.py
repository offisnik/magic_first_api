import httpx as x
from faker import Faker
fake = Faker()


# Получение нового Токена
def get_token():
    response = x.post('https://aqa-proka4.org/sandbox/api/reset-token')
    my_token = response.json()['bearer_token']
    return my_token

# передача заголовка полностью в запросы
def get_headers():
    headers = {"Authorization": f"{get_token()}",
    "user-agent": fake.chrome(),
    "Cookie": "session=78c2a549-323c-4005-a783-f1bd18b08c18.1uUTJ8Rq6DpQHTyuH36SuBPh8ys"}
    return headers
