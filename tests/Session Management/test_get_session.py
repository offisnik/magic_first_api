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

