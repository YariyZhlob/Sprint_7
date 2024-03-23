import pytest
from helpers import *
import requests
import json
from constants import Constants
import requests


@allure.story('Test of courier creation')
class TestCreationCourier:
    @allure.title('it is possible to create a courier')
    def test_courier_creation(self):
        response = requests.post(url=Constants.COURIER_REGISTRATION, data=create_payload())
        assert response.status_code == 201
        assert response.json() == json.loads('{"ok":true}')


    @allure.title('it is impossible to create two identical couriers')
    def test_creation_two_identical_couriers(self):
        requests.post(url=Constants.COURIER_REGISTRATION,
                                             data=create_courier_payload_with_known_params(
                                                 login=Constants.COURIER_KNOWN_LOGIN,
                                                 password=Constants.COURIER_KNOWN_PASSWORD,
                                                 first_name=Constants.COURIER_KNOWN_FIRST_NAME
                                             ))
        response_courier_two = requests.post(url=Constants.COURIER_REGISTRATION,
                                             data=create_courier_payload_with_known_params(
                                                 login=Constants.COURIER_KNOWN_LOGIN,
                                                 password=Constants.COURIER_KNOWN_PASSWORD,
                                                 first_name=Constants.COURIER_KNOWN_FIRST_NAME
                                             ))

        assert response_courier_two.status_code == 409
        assert response_courier_two.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('to create a courier it is necessary to transmit all necessary fields')
    def test_creation_courier_without_login(self):
        response = requests.post(url=Constants.COURIER_REGISTRATION,
                                 data={"password": password_creation(),
                                       "first_name": first_name_creation()})
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

