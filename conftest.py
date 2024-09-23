import pytest
from faker import Faker
from endpoints.delete_user import DeleteUser

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
