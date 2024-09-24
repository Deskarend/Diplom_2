import allure
import pytest

from endpoints.base_endpoint import BaseEndpoint
from endpoints.edit_user_data import EditUserData


class TestEditUserData:

    @allure.title("Проверка изменения данных пользователя")
    @allure.description('При успешном изменении данных пользователя код ответа 200, тело ответа содержит "success":'
                        ' true", email и name корректно изменяются')
    @pytest.mark.parametrize('regenerate_field', [BaseEndpoint.regenerate_email,
                                                  BaseEndpoint.regenerate_password,
                                                  BaseEndpoint.regenerate_name])
    def test_edit_user_data(self, payload_of_new_courier, token_for_authorization, regenerate_field):
        edited_field = regenerate_field(payload_of_new_courier)
        edit_user_data = EditUserData()

        edit_user_data.edit_user_data(edited_field, token_for_authorization)

        edit_user_data.check_response_of_successful_edit_user_data(edited_field)

    @allure.title("Проверка изменения данных пользователя без авторизации")
    @allure.description('При изменении данных пользователя без авторизации код ответа 401, '
                        'тело - {"success": False, "message": "You should be authorised"}')
    @pytest.mark.parametrize('regenerate_field', [BaseEndpoint.regenerate_email,
                                                  BaseEndpoint.regenerate_password,
                                                  BaseEndpoint.regenerate_name])
    def test_edit_user_data_without_authorization(self, payload_of_new_courier, regenerate_field):
        edited_field = regenerate_field(payload_of_new_courier)
        edit_user_data = EditUserData()

        edit_user_data.edit_user_data(edited_field)

        edit_user_data.check_response_body_of_edit_user_data_without_authorization()
