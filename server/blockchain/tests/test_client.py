import json
from django.test import SimpleTestCase, Client


class RequestTests(SimpleTestCase):

    def login_client_user(self):
        client = Client()
        response = client.post('/login/', {'username': 'admin', 'password': 'admin'})
        assert response.status_code == 302

    def logout_client_user(self):

        response = self.client.logout()
        assert response.status_code == 200

    def is_json(myjson):

        """
        tests if a string is valid JSON
        """
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True
