import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class LoginUser(BaseEndpoint):
    LOGIN_USER_ENDPOINT = 'api/auth/login'

    STATUS_CODE_OF_SUCCESSFUL_LOGIN_USER = 200

    STATUS_CODE_OF_LOGIN_USER_WITH_INCORRECT_FIELD = 401
    RESPONSE_BODY_OF_LOGIN_USER_WITH_INCORRECT_FIELD = {"success": False,
                                                        "message": "email or password are incorrect"}

    @allure.step('Авторизация пользователя')
    def login(self, payload):
        url = self.BASE_URL + self.LOGIN_USER_ENDPOINT
        self.response = requests.post(url, json=payload)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешной авторизации пользователя')
    def check_response_status_code_of_successful_login_user(self):
        self._check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_LOGIN_USER)

    @allure.step('Проверка тело ответа успешной авторизации пользователя')
    def check_response_body_of_login_user(self, payload):
        assert self.response_json['success'] is True, (f'Ожидаемое значение поля success - {True}, '
                                                       f'фактическое - {self.response_json['success']}')
        assert self.response_json['user']['email'] == payload['email'], \
            f'Ожидаемое значение поля email - {payload['email']}, фактическое - {self.response_json['user']['email']} '
        assert 'Bearer ' in self.response_json['accessToken'], f'Ожидаемое значение поля accessToken - Bearer ...'
        assert self.response_json['refreshToken'], f'Ожидаемое значение поля refreshToken - непустое'

    @allure.step('Проверка ответа успешной авторизации пользователя')
    def check_response_of_successful_login_user(self, payload):
        self.check_response_status_code_of_successful_login_user()
        self.check_response_body_of_login_user(payload)

    @allure.step('Проверка статус кода авторизации пользователя c неверным логином и паролем')
    def check_response_status_code_login_user_with_incorrect_field(self):
        self._check_response_status_code(self.STATUS_CODE_OF_LOGIN_USER_WITH_INCORRECT_FIELD)

    @allure.step('Проверка тело ответа авторизации пользователя c неверным логином и паролем')
    def check_response_body_of_login_user_with_incorrect_field(self):
        self._check_response_body(self.RESPONSE_BODY_OF_LOGIN_USER_WITH_INCORRECT_FIELD)

    @allure.step('Проверка ответа авторизации пользователя неверным c логином и паролем')
    def check_response_of_login_user_with_incorrect_field(self):
        self.check_response_status_code_login_user_with_incorrect_field()
        self.check_response_body_of_login_user_with_incorrect_field()