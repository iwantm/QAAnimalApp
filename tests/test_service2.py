from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from requests.api import request
import requests
from service2.app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestApi(TestBase):
    def test_get_animal(self):
        response = self.client.get(url_for('random_animal'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'animal', response.data)

    def test_post_animal(self):
        response = self.client.post(
            url_for('animal_sound'), json={"animal": "frog"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ribbit', response.data)
