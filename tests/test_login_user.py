import allure
import pytest

from endpoints.base_endpoint import BaseEndpoint
from endpoints.login_user import LoginUser


class TestLoginUser:
    @allure.title("Проверка авторизация зарегистрированного пользователя")
    @allure.description('При успешной авторизации пользователя код ответа 200, тело ответа содержит "success": true",'
                        'email соответствуют введенному при авторизации, а также непустые токены: accessToken и '
                        'refreshToken')
    def test_login_user(self, payload_for_authorization):
        login_user = LoginUser()

        login_user.login(payload_for_authorization)

        login_user.check_response_of_successful_login_user(payload_for_authorization)

    @allure.title("Проверка авторизации пользователя c неверным логином и паролем")
    @allure.description('При авторизации пользователя c неверным логином и паролем код ответа: 401, '
                        'тело - {"success": False, "message": "email or password are incorrect"}')
    @pytest.mark.parametrize('regenerate_field', [BaseEndpoint.regenerate_email,
                                                  BaseEndpoint.regenerate_password,
                                                  BaseEndpoint.regenerate_email_and_password])
    def test_login_with_incorrect_field(self, regenerate_field, payload_for_authorization):
        login_user = LoginUser()
        incorrect_payload = regenerate_field(payload_for_authorization)

        login_user.login(incorrect_payload)

        login_user.check_response_of_login_user_with_incorrect_field()
