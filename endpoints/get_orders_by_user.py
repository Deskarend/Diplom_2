import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class GetOrdersByUser(BaseEndpoint):
    GET_ORDERS_BY_USERS = 'api/orders'

    STATUS_CODE_OF_SUCCESSFUL_GET_ORDERS_BY_USER = 200

    STATUS_CODE_OF_GET_ORDERS_BY_USER_WITHOUT_AUTHORIZATION = 401
    RESPONSE_BODY_OF_GET_ORDERS_BY_USER_WITHOUT_AUTHORIZATION = {"success": False,
                                                                 "message": "You should be authorised"}

    @allure.step('Получение заказов конкретного пользователя')
    def get_orders_by_user(self, token=None):
        url = self.BASE_URL + self.GET_ORDERS_BY_USERS
        if token:
            self.response = requests.get(url, headers={"Authorization": token})
        else:
            self.response = requests.get(url)
        self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного получения заказов конкретного пользователя')
    def check_response_status_code_of_successful_get_orders_by_user(self):
        self._check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_GET_ORDERS_BY_USER)

    @allure.step('Проверка тело ответа успешного получения заказов конкретного пользователя')
    def check_response_body_of_successful_get_orders_by_user(self):
        assert self.response_json['success'] is True, (f'Ожидаемое значение поля success - {True}, '
                                                       f'фактическое - {self.response_json['success']}')
        assert self.response_json['orders'], (f'Ожидаемое значение поля orders - непустое, '
                                              f'фактическое - {self.response_json['orders']}')
        assert self.response_json['total'], (f'Ожидаемое значение поля total - непустое, '
                                             f'фактическое - {self.response_json['total']}')
        assert self.response_json['totalToday'], (f'Ожидаемое значение поля totalToday - непустое, '
                                                  f'фактическое - {self.response_json['totalToday']}')

    @allure.step('Проверка ответа успешного получения заказов конкретного пользователя')
    def check_response_of_successful_get_orders_by_user(self):
        self.check_response_status_code_of_successful_get_orders_by_user()
        self.check_response_body_of_successful_get_orders_by_user()

    @allure.step('Проверка статус кода получения заказов конкретного пользователя без авторизации')
    def check_response_status_code_of_get_orders_by_user_without_authorization(self):
        self._check_response_status_code(self.STATUS_CODE_OF_GET_ORDERS_BY_USER_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка тело ответа получения заказов конкретного пользователя без авторизации')
    def check_response_body_of_get_orders_by_user_without_authorization(self):
        self._check_response_body(self.RESPONSE_BODY_OF_GET_ORDERS_BY_USER_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка ответа создания получения заказов конкретного пользователя без авторизации')
    def check_response_of_get_orders_by_user_without_authorization(self):
        self.check_response_status_code_of_get_orders_by_user_without_authorization()
        self.check_response_body_of_get_orders_by_user_without_authorization()
