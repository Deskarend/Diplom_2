import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateUser(BaseEndpoint):
    CREATE_USER_ENDPOINT = 'api/auth/register'

    STATUS_CODE_OF_SUCCESSFUL_CREATE_USER = 200

    STATUS_CODE_OF_CREATE_THE_SAME_USERS = 403
    RESPONSE_BODY_CREATE_THE_SAME_USERS = {"success": False, "message": "User already exists"}

    STATUS_CODE_OF_CREATE_USER_WITHOUT_REQUIRED_FIELDS = 403
    RESPONSE_BODY_OF_CREATE_USER_WITHOUT_REQUIRED_FIELDS = {"success": False,
                                                            "message": "Email, password and name are required fields"}

    @allure.step('Создание курьера')
    def create_user(self, payload):
        url = self.BASE_URL + self.CREATE_USER_ENDPOINT
        self.response = requests.post(url, json=payload)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного создания пользователя')
    def check_response_status_code_of_successful_create_user(self):
        self._check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_CREATE_USER)

    @allure.step('Проверка тело ответа успешного создания пользователя')
    def check_response_body_of_created_user(self, payload):
        assert self.response_json['success'] is True, (f'Ожидаемое значение поля success - {True}, '
                                                       f'фактическое - {self.response_json['success']}')
        assert self.response_json['user']['email'] == payload['email'], \
            f'Ожидаемое значение поля email - {payload['email']}, фактическое - {self.response_json['user']['email']} '

        assert self.response_json['user']['name'] == payload['name'], \
            f'Ожидаемое значение поля name - {payload['name']}, фактическое - {self.response_json['user']['name']}'
        assert 'Bearer ' in self.response_json['accessToken'], (f'Ожидаемое значение поля accessToken - Bearer ..., '
                                                                f'фактическое {self.response_json['accessToken']}')
        assert self.response_json['refreshToken'], (f'Ожидаемое значение поля refreshToken - непустое,'
                                                    f'фактическое {self.response_json['refreshToken']}')

    @allure.step('Проверка ответа успешного создания пользователя')
    def check_response_of_successful_create_user(self, payload):
        self.check_response_status_code_of_successful_create_user()
        self.check_response_body_of_created_user(payload)

    @allure.step('Проверка статус кода создания одинаковых пользователей')
    def check_response_status_code_of_create_the_same_user(self):
        self._check_response_status_code(self.STATUS_CODE_OF_CREATE_THE_SAME_USERS)

    @allure.step('Проверка тело ответа создания одинаковых пользователей')
    def check_response_body_of_create_the_same_users(self):
        self._check_response_body(self.RESPONSE_BODY_CREATE_THE_SAME_USERS)

    @allure.step('Проверка ответа создания одинаковых пользователей')
    def check_response_of_create_the_same_users(self):
        self.check_response_status_code_of_create_the_same_user()
        self.check_response_body_of_create_the_same_users()

    @allure.step('Проверка статус кода создания пользователя без обязательных полей')
    def check_response_status_code_of_create_user_without_required_fields(self):
        self._check_response_status_code(self.STATUS_CODE_OF_CREATE_USER_WITHOUT_REQUIRED_FIELDS)

    @allure.step('Проверка тело ответа создания пользователя без обязательных полей')
    def check_response_body_of_create_user_without_required_fields(self):
        self._check_response_body(self.RESPONSE_BODY_OF_CREATE_USER_WITHOUT_REQUIRED_FIELDS)

    @allure.step('Проверка ответа создания пользователя без обязательных полей')
    def check_response_of_create_user_without_required_fields(self):
        self.check_response_status_code_of_create_user_without_required_fields()
        self.check_response_body_of_create_user_without_required_fields()
