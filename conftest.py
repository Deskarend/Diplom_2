import pytest
from faker import Faker

from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser
from endpoints.login_user import LoginUser

fake = Faker(locale='ru_RU')


@pytest.fixture
def payload_of_new_courier():
    payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }

    yield payload

    payload_for_check_authorization = {
        "email": payload['email'],
        "password": payload['password']
    }

    login_user = LoginUser()
    login_user.login(payload_for_check_authorization)
    if login_user.response.status_code == 200:
        DeleteUser().delete_user(login_user.get_access_token())


@pytest.fixture
def payload_for_authorization(payload_of_new_courier):
    create_user = CreateUser()

    create_user.create_user(payload_of_new_courier)

    payload = {
        "email": payload_of_new_courier['email'],
        "password": payload_of_new_courier['password']
    }
    return payload


@pytest.fixture
def token_for_authorization(payload_for_authorization):
    login_user = LoginUser()
    login_user.login(payload_for_authorization)
    yield login_user.get_access_token()
    DeleteUser().delete_user(login_user.get_access_token())
