import pytest
from faker import Faker

from endpoints.create_user import CreateUser

# from endpoints.delete_user import DeleteUser

fake = Faker(locale='ru_RU')


@pytest.fixture
def payload_of_new_courier():
    payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }
    return payload

    # yield payload
    # delete_user = DeleteUser()
    # delete_user.delete_user()


@pytest.fixture()
def payload_for_authorization(payload_of_new_courier):
    create_user = CreateUser()

    create_user.create_user(payload_of_new_courier)

    payload = {
        "email": payload_of_new_courier['email'],
        "password": payload_of_new_courier['password']
    }
    return payload
