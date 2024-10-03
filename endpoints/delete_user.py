import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteUser(BaseEndpoint):
    DELETE_USER_ENDPOINT = 'api/auth/user'

    def delete_user(self, token):
        self.response = requests.delete(self.BASE_URL + self.DELETE_USER_ENDPOINT,
                                        headers={'Authorization': token})
