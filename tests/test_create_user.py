import allure
import pytest

from endpoints.base_endpoint import BaseEndpoint
from endpoints.create_user import CreateUser


class TestCreateUser:
    @allure.title("Проверка создания нового пользователя")
    @allure.description('При успешном создании пользователя код ответа 200, тело ответа содержит "success": true",'
                        'email и name соответствуют при регистрации, а также непустые токены: accessToken и '
                        'refreshToken')
    def test_create_user(self, payload_of_new_courier):
        create_courier = CreateUser()

        create_courier.create_user(payload_of_new_courier)

        create_courier.check_response_of_successful_create_user(payload_of_new_courier)

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    @allure.description('При создании двух одинаковых пользователей код ответа: 403, '
                        'тело - {"success": False, "message": "User already exists"}')
    def test_create_the_same_user_twice(self, payload_of_new_courier):
        create_courier = CreateUser()

        create_courier.create_user(payload_of_new_courier)
        create_courier.create_user(payload_of_new_courier)

        create_courier.check_response_of_create_the_same_users()

    @allure.title("Проверка создания пользователя без обязательных полей")
    @allure.description('При создании пользователя без обязательных полей код ответа: 403, '
                        'тело - {"success": False, "message":  "Email, password and name are required fields"}')
    @pytest.mark.parametrize('generate_payload_without_required_field', [BaseEndpoint.delete_email_from_payload,
                                                                         BaseEndpoint.delete_password_from_payload,
                                                                         BaseEndpoint.delete_name_from_payload])
    def test_create_user_without_required_fields(self, payload_of_new_courier, generate_payload_without_required_field):
        create_courier = CreateUser()
        invalid_payload = generate_payload_without_required_field(payload_of_new_courier)

        create_courier.create_user(invalid_payload)

        create_courier.check_response_of_create_user_without_required_fields()
