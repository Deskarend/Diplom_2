import allure

import data
from endpoints.create_order import CreateOrder
from endpoints.get_orders_by_user import GetOrdersByUser


class TestGetOrdersByUser:
    @allure.title("Проверка получения заказов конкретного пользователя")
    @allure.description('При успешном получении заказов конкретного пользователя код ответа 200, '
                        'тело ответа содержит "success": true", непустые total, totalToday и orders ')
    def test_get_orders_by_user(self, token_for_authorization):
        create_order = CreateOrder()
        burger_1 = data.Burgers.burger_1
        burger_2 = data.Burgers.burger_2
        create_order.create_order(burger_1, token_for_authorization)
        create_order.create_order(burger_2, token_for_authorization)

        get_orders_by_user = GetOrdersByUser()
        get_orders_by_user.get_orders_by_user(token_for_authorization)

        get_orders_by_user.check_response_of_successful_get_orders_by_user()

    @allure.title("Проверка получения заказов конкретного пользователя без авторизации")
    @allure.description('При получении заказов конкретного пользователя без авторизации код ответа 401, '
                        'тело ответа - {"success": False, "message": "You should be authorised"}')
    def test_get_orders_by_user_without_authorization(self, token_for_authorization):
        create_order = CreateOrder()
        burger_1 = data.Burgers.burger_1
        burger_2 = data.Burgers.burger_2
        create_order.create_order(burger_1, token_for_authorization)
        create_order.create_order(burger_2, token_for_authorization)

        get_orders_by_user = GetOrdersByUser()
        get_orders_by_user.get_orders_by_user()

        get_orders_by_user.check_response_of_get_orders_by_user_without_authorization()
