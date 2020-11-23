from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from requests.api import request
import requests
from service1.app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.json.return_value = {"animal": "frog"}
                p.return_value.json.return_value = {"sound": "ribbit"}
                response = self.client.get(url_for('index'))
                self.assertIn(b'frog', response.data)
                self.assertIn(b'ribbit', response.data)
