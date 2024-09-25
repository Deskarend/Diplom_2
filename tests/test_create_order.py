import allure

import data
from endpoints.create_order import CreateOrder


class TestCreateOrder:
    @allure.title("Проверка создания нового заказа")
    @allure.description('При успешном создании заказа код ответа 200, тело ответа содержит "success": true",'
                        'непустой name и номер заказа(number) в order')
    def test_create_order(self, token_for_authorization):
        create_order = CreateOrder()
        payload = data.Burgers.burger_1
        access_token = token_for_authorization

        create_order.create_order(payload, access_token)

        create_order.check_response_of_successful_create_order()

    @allure.title("Проверка создания нового заказа без авторизации")
    @allure.description('При создании заказа без авторизации код ответа 401, '
                        'тело ответа - {"success": False, "message": "You should be authorised"}')
    def test_create_order_without_authorization(self):
        create_order = CreateOrder()
        payload = data.Burgers.burger_1

        create_order.create_order(payload)

        create_order.check_response_body_of_create_order_without_authorization()

    @allure.title("Проверка создания заказа без ингредиентов")
    @allure.description('При создании заказа без ингредиентов код ответа 400, '
                        'тело ответа - {"success": False, "message": "Ingredient ids must be provided"}')
    def test_create_order_without_ingredients(self, token_for_authorization):
        create_order = CreateOrder()
        payload = data.Burgers.burger_with_no_ingredients
        access_token = token_for_authorization

        create_order.create_order(payload, access_token)

        create_order.check_response_of_create_order_without_ingredients()

    @allure.title("Проверка создания заказа c неверным хешем ингредиентов")
    @allure.description('При создании заказа c неверным хешем ингредиентов код ответа 500')
    def test_create_order_with_incorrect_hash_ingredients(self, token_for_authorization):
        create_order = CreateOrder()
        payload = data.Burgers.burger_with_incorrect_hashes
        access_token = token_for_authorization

        create_order.create_order(payload, access_token)

        create_order.check_response_of_create_order_with_incorrect_hashes_ingredients()


