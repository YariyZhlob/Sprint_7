import pytest
from helpers import *
import requests
import json
from constants import Constants
import requests


@allure.story('Test order list return')
class TestOrderList:
    @allure.title('Test order list return')
    def test_return_order_list(self):
        response = requests.get(url=Constants.RETURN_ORDER_LIST).json()
        assert "orders" in response

