import httpx as x
from conftest import get_headers



class GetSession:
    status_code = None
    bearer_token = None
    is_authenticated = None
    limits = None
    max_resource_size = None
    max_resources_per_type = None
    ttl = None
    session_id = None
    storage = None
    user_id = None
    all_data = None

    def get_session_info(self):
        response = x.get('https://aqa-proka4.org/sandbox/api/session', headers=get_headers())

        self.all_data = response.json()
        self.status_code = response.status_code
        self.bearer_token = response.json()['bearer_token']
        self.is_authenticated = True
        self.limits = response.json()['limits']
        self.max_resource_size = response.json()['limits']['max_resource_size']
        self.max_resources_per_type = response.json()['limits']['max_resources_per_type']
        self.ttl = response.json()['limits']['ttl']
        self.session_id = response.json()['session_id']
        self.storage = response.json()['storage']
        self.user_id = response.json()['user_id']
        return response

    def check_code_answer(self):
        assert self.status_code == 200, f'Ошибка в статус коде, пришло = {self.status_code}'


    def check_parameters_in_response(self):
        assert "bearer_token" in self.all_data.keys(), f'Ошибка отсутствует параметр "bearer_token" в ответе'
        assert "is_authenticated" in self.all_data.keys(), f'Ошибка отсутствует параметр "is_authenticated" в ответе'
        assert "limits" in self.all_data.keys(), f'Ошибка отсутствует параметр "limits" в ответе'

        assert "max_resource_size" in self.all_data["limits"], f'Ошибка отсутствует параметр "max_resource_size" в ответе'
        assert "max_resources_per_type" in self.all_data["limits"], f'Ошибка отсутствует параметр "max_resources_per_type" в ответе'
        assert "ttl" in self.all_data["limits"], f'Ошибка отсутствует параметр "ttl" в ответе'

        assert "session_id" in self.all_data.keys(), f'Ошибка отсутствует параметр "session_id" в ответе'
        assert "storage" in self.all_data.keys(), f'Ошибка отсутствует параметр "storage" в ответе'
        assert "user_id" in self.all_data.keys(), f'Ошибка отсутствует параметр "user_id" в ответе'


    def check_meanings_parameters_in_response(self):
        assert self.all_data["is_authenticated"] == True, f'Ошибка параметр "is_authenticated" != True, вместо него {self.all_data["is_authenticated"]} в ответе'
        assert self.all_data["limits"]["max_resource_size"] == 10240, f'Ошибка в значении параметра "max_resource_size", вместо 10240 в ответе {self.all_data["limits"]["max_resource_size"]}'
        assert self.all_data["limits"]["max_resources_per_type"] == 100, f'Ошибка в параметре "max_resources_per_type" вместо 100 в ответе {self.all_data["limits"]["max_resources_per_type"]}'
        assert self.all_data["limits"]["ttl"] == "permanent", f'Ошибка в параметре "ttl" в ответе == {self.all_data["limits"]["ttl"]}'
        assert self.all_data["storage"] == "postgresql", f'Ошибка в значении "storage", пришло {self.all_data["storage"]}'
        assert self.all_data["user_id"] == 524, f'Ошибка в значении "user_id" в ответе {self.all_data["user_id"]}'