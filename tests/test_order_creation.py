import pytest
from helpers import *
import requests
import json
from constants import Constants
import requests


@allure.story('Test order creation')
class TestOrderCreation:
    @allure.title('Test one of colors, both colors, without colors')
    @pytest.mark.parametrize("color", Constants.COLORS)
    def test_order_creation(self, color):
        response = requests.post(url=Constants.CREATE_ORDER, data=Constants.PAYLOAD.update({"color": color}))
        assert 'track' in response.json()


