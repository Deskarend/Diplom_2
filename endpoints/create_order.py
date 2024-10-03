import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateOrder(BaseEndpoint):
    CREATE_ORDER_ENDPOINT = 'api/orders'

    STATUS_CODE_OF_SUCCESSFUL_CREATE_ORDER = 200

    STATUS_CODE_OF_CREATE_ORDER_WITHOUT_AUTHORIZATION = 401
    RESPONSE_BODY_OF_CREATE_ORDER_WITHOUT_AUTHORIZATION = {"success": False, "message": "You should be authorised"}

    STATUS_CODE_OF_CREATE_ORDER_WITHOUT_INGREDIENTS = 400
    RESPONSE_BODY_OF_CREATE_ORDER_WITHOUT_INGREDIENTS = {"success": False, "message": "Ingredient ids must be provided"}

    STATUS_CODE_OF_CREATE_ORDER_WITH_INCORRECT_HASH_INGREDIENTS = 500

    @allure.step('Создание заказа')
    def create_order(self, payload, token=None):
        url = self.BASE_URL + self.CREATE_ORDER_ENDPOINT
        if token:
            self.response = requests.post(url, json=payload, headers={"Authorization": token})
        else:
            self.response = requests.post(url, payload)
        if '5' not in str(self.response.status_code):
            self.response_json = self.response.json()

    @allure.step('Проверка статус кода успешного создания заказа')
    def check_response_status_code_of_successful_create_order(self):
        self._check_response_status_code(self.STATUS_CODE_OF_SUCCESSFUL_CREATE_ORDER)

    @allure.step('Проверка тело ответа успешного создания заказа')
    def check_response_body_of_created_order(self):
        assert self.response_json['name'], (f'Ожидаемое значение поля name - непустое, фактическое -'
                                            f' {self.response_json['name']}')
        assert self.response_json['order']['number'], (f'Ожидаемое значение поля number - непустое, '
                                                       f'фактическое - {self.response_json['user']['number']}')
        assert self.response_json['success'] is True, (f'Ожидаемое значение поля success - {True}, '
                                                       f'фактическое - {self.response_json['success']}')

    @allure.step('Проверка ответа успешного создания заказа')
    def check_response_of_successful_create_order(self):
        self.check_response_status_code_of_successful_create_order()
        self.check_response_body_of_created_order()

    @allure.step('Проверка статус кода создания заказа без авторизации')
    def check_response_status_code_of_create_order_without_authorization(self):
        self._check_response_status_code(self.STATUS_CODE_OF_CREATE_ORDER_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка тело ответа создания заказа без авторизации')
    def check_response_body_of_create_order_without_authorization(self):
        self._check_response_body(self.RESPONSE_BODY_OF_CREATE_ORDER_WITHOUT_AUTHORIZATION)

    @allure.step('Проверка ответа создания заказа без авторизации')
    def check_response_of_create_order_without_authorization(self):
        self.check_response_status_code_of_create_order_without_authorization()
        self.check_response_body_of_create_order_without_authorization()

    @allure.step('Проверка статус кода создания заказа без ингредиентов')
    def check_response_status_code_of_create_order_without_ingredients(self):
        self._check_response_status_code(self.STATUS_CODE_OF_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.step('Проверка тело ответа создания заказа без ингредиентов')
    def check_response_body_of_create_order_without_ingredients(self):
        self._check_response_body(self.RESPONSE_BODY_OF_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.step('Проверка ответа создания заказа без ингредиентов')
    def check_response_of_create_order_without_ingredients(self):
        self.check_response_status_code_of_create_order_without_ingredients()
        self.check_response_body_of_create_order_without_ingredients()

    @allure.step('Проверка ответа создания заказа c неверным хешем ингредиентов')
    def check_response_of_create_order_with_incorrect_hashes_ingredients(self):
        self._check_response_status_code(self.STATUS_CODE_OF_CREATE_ORDER_WITH_INCORRECT_HASH_INGREDIENTS)
