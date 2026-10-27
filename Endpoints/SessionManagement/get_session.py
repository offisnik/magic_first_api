import httpx as x
from Endpoints.cheks_for_every import EveryCheckes
from conftest import get_headers
from pydantic import BaseModel, Field


class CheckParamsLimits(BaseModel):
    max_resource_size: int
    max_resources_per_type: int
    ttl: str


class CheckParamsAll(BaseModel):
    bearer_token: str
    is_authenticated: bool
    limits: CheckParamsLimits
    session_id: str
    storage: str
    user_id: int


class CheckParamsNoToken(BaseModel):
    error: str = Field(pattern="Authorization required")
    example: str = Field(pattern="Authorization: Bearer sandbox_xxx...")
    message: str = Field(pattern="Use Bearer token in Authorization header or access via web interface")


class GetSession(EveryCheckes):
    all_data = None

    def get_session_info(self):
        response = x.get('https://aqa-proka4.org/sandbox/api/session', headers=get_headers())
        self.all_data = response.json()
        self.status_code = response.status_code
        return response


    def check_parameters_in_response(self):
        CheckParamsAll(**self.all_data)


    def check_meanings_parameters_in_response(self):
        assert self.all_data["is_authenticated"] == True, f'Ошибка параметр "is_authenticated" != True, вместо него {self.all_data["is_authenticated"]} в ответе'
        assert self.all_data["limits"]["max_resource_size"] == 10240, f'Ошибка в значении параметра "max_resource_size", вместо 10240 в ответе {self.all_data["limits"]["max_resource_size"]}'
        assert self.all_data["limits"]["max_resources_per_type"] == 100, f'Ошибка в параметре "max_resources_per_type" вместо 100 в ответе {self.all_data["limits"]["max_resources_per_type"]}'
        assert self.all_data["limits"]["ttl"] == "permanent", f'Ошибка в параметре "ttl" в ответе == {self.all_data["limits"]["ttl"]}'
        assert self.all_data["storage"] == "postgresql", f'Ошибка в значении "storage", пришло {self.all_data["storage"]}'
        assert self.all_data["user_id"] == 524, f'Ошибка в значении "user_id" в ответе {self.all_data["user_id"]}'

    def check_wrong_method(self):
        response = x.post('https://aqa-proka4.org/sandbox/api/session', headers=get_headers())
        assert response.status_code == 405, f'Ожидаем код POST ответа 405, пришел код {response.status_code}'

        response = x.put('https://aqa-proka4.org/sandbox/api/session', headers=get_headers())
        assert response.status_code == 405, f'Ожидаем код PUT ответа 405, пришел код {response.status_code}'

        response = x.patch('https://aqa-proka4.org/sandbox/api/session', headers=get_headers())
        assert response.status_code == 405, f'Ожидаем код PATCH ответа 405, пришел код {response.status_code}'

    def check_no_token(self):
        response = x.get('https://aqa-proka4.org/sandbox/api/session')
        self.all_data = response.json()
        return response

    def check_parameters_in_response_no_token(self):
        CheckParamsNoToken(**self.all_data)

    def check_meanings_parameters_in_response_no_token(self):
        CheckParamsNoToken(**self.all_data)
