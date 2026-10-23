"""
GET запрос, который получает данные сессии
"""

import httpx as x


"""
Позитивные кейсы
"""

def test_get_session_info(get_token):
    headers = {"Authorization": f"Bearer {get_token}",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
               "Cookie": "session=78c2a549-323c-4005-a783-f1bd18b08c18.1uUTJ8Rq6DpQHTyuH36SuBPh8ys"}
    response = x.get('https://aqa-proka4.org/sandbox/api/session', headers=headers)
    print(response.json())

    assert response.status_code == 200, f'Ошибка в статус коде, пришло = {response.status_code}'
    assert "bearer_token" in response.json().keys(), f'Ошибка отсутствует параметр "bearer_token" в ответе'
    assert "is_authenticated" in response.json().keys(), f'Ошибка отсутствует параметр "is_authenticated" в ответе'
    assert "limits" in response.json().keys(), f'Ошибка отсутствует параметр "limits" в ответе'

    assert "max_resource_size" in response.json()["limits"], f'Ошибка отсутствует параметр "max_resource_size" в ответе'
    assert "max_resources_per_type" in response.json()["limits"], f'Ошибка отсутствует параметр "max_resources_per_type" в ответе'
    assert "ttl" in response.json()["limits"], f'Ошибка отсутствует параметр "ttl" в ответе'

    assert "session_id" in response.json().keys(), f'Ошибка отсутствует параметр "session_id" в ответе'
    assert "storage" in response.json().keys(), f'Ошибка отсутствует параметр "storage" в ответе'
    assert "user_id" in response.json().keys(), f'Ошибка отсутствует параметр "user_id" в ответе'



"""
Негативные кейсы
"""

