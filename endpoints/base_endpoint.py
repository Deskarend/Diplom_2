class BaseEndpoint:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    response = None
    response_json = None

    def _check_response_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Ожидаемый код ответа:{status_code}, '
                                                          f'фактический:{self.response.status_code}')

    def _check_response_body(self, response_body):
        assert self.response_json == response_body, (f'Ожидаемое тело ответа:{response_body}, '
                                                     f'фактический:{self.response_json}')

    @staticmethod
    def _delete_field_from_payload(field, payload):
        new_payload = payload.copy()
        new_payload[field] = ''
        return new_payload

    @staticmethod
    def delete_email_from_payload(payload):
        return BaseEndpoint._delete_field_from_payload('email', payload)

    @staticmethod
    def delete_password_from_payload(payload):
        return BaseEndpoint._delete_field_from_payload('password', payload)

    @staticmethod
    def delete_name_from_payload(payload):
        return BaseEndpoint._delete_field_from_payload('name', payload)
