"""
GET запрос, который получает все данные нашей сессии и пользователя с токеном
"""
from Endpoints.SessionManagement.get_session import GetSession

"""
Позитивные кейсы
"""

def test_get_session_info():
    get_session_endpoint = GetSession()
    get_session_endpoint.get_session_info()
    get_session_endpoint.status_code()
    get_session_endpoint.check_parameters_in_response()
    get_session_endpoint.check_meanings_parameters_in_response()


"""
Негативные кейсы
"""

def test_get_session_wrong():
    wrong_method = GetSession()
    wrong_method.check_wrong_method()


def test_no_token():
    no_token = GetSession()
    no_token.check_no_token()
    no_token.check_parameters_in_response_no_token()
    no_token.check_meanings_parameters_in_response_no_token()