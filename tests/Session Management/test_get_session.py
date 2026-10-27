"""
GET запрос, который получает все данные нашей сессии и пользователя с токеном
"""
from Endpoints.SessionManagement.get_session import GetSession

"""
Позитивные кейсы
"""

def test_get_session_info():
    get_session_init = GetSession()
    get_session_init.get_session_info()
    get_session_init.check_code_answer()
    get_session_init.check_parameters_in_response()
    get_session_init.check_meanings_parameters_in_response()


"""
Негативные кейсы
"""

def test_get_session_wrong():
    get_session_init = GetSession()
    get_session_init.check_wrong_method()


def test_no_token():
    get_session_init = GetSession()
    get_session_init.check_no_token()
    get_session_init.check_parameters_in_response_no_token()
    get_session_init.check_meanings_parameters_in_response_no_token()