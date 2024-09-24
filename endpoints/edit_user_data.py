import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class EditUserData(BaseEndpoint):
    EDIT_USER_DATA_ENDPOINT = '/api/auth/user'

    STATUS_CODE_OF_SUCCESSFUL_EDIT_USER_DATA = 200

    STATUS_CODE_OF_EDIT_USER_DATA_WITHOUT_AUTHORIZATION = 401
    RESPONSE_BODY_OF_EDIT_USER_DATA_WITHOUT_AUTHORIZATION = {"success": False, "message": "You should be authorised"}

    @allure.step('Изменение данных пользователя')
    def edit_user_data(self, payload, token=None):
        url = self.BASE_URL + self.EDIT_USER_DATA_ENDPOINT
        if token:
            self.response = requests.patch(url, payload, headers={'Authorization': token})
        else:
            self.response = requests.patch(url, payload)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного изменения данных пользователя')
    def check_response_status_code_of_successful_edit_user_data(self):
        self._check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_EDIT_USER_DATA)

    @allure.step('Проверка тело ответа успешного изменения данных пользователя')
    def check_response_body_of_successful_edit_user_data(self, payload):
        assert self.response_json['success'] is True, (f'Ожидаемое значение поля success - {True}, '
                                                       f'фактическое - {self.response_json['success']}')
        assert self.response_json['user']['email'] == payload['email'], \
            f'Ожидаемое значение поля email - {payload['email']}, фактическое - {self.response_json['user']['email']} '

        assert self.response_json['user']['name'] == payload['name'], \
            f'Ожидаемое значение поля name - {payload['name']}, фактическое - {self.response_json['user']['name']}'

    @allure.step('Проверка ответа успешного изменения данных пользователя')
    def check_response_of_successful_edit_user_data(self, payload):
        self.check_response_status_code_of_successful_edit_user_data()
        self.check_response_body_of_successful_edit_user_data(payload)

    @allure.step('Проверка статус кода изменения данных пользователя без авторизации')
    def check_response_status_code_of_edit_user_data_without_authorization(self):
        self._check_response_status_code(self.STATUS_CODE_OF_EDIT_USER_DATA_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка тело ответа изменения данных пользователя без авторизации')
    def check_response_body_of_edit_user_data_without_authorization(self):
        self._check_response_body(self.RESPONSE_BODY_OF_EDIT_USER_DATA_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка ответа изменения данных пользователя без авторизации')
    def check_response_of_edit_user_data_without_authorization(self):
        self.check_response_status_code_of_edit_user_data_without_authorization()
        self.check_response_body_of_edit_user_data_without_authorization()
