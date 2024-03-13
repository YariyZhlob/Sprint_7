import pytest
from conftest import *
import requests
import json
from constants import Constants
import requests


@allure.story('Test of courier login')
class TestLoginCourier:
    @allure.title('Courier can login')
    def test_courier_can_login(self):
        data = create_payload()
        courier = requests.post(url=Constants.COURIER_REGISTRATION, data=data)
        response = requests.post(url=Constants.COURIER_LOGIN, data=data)
        assert response.status_code == 200
        assert "id" in response.text


    @allure.title('Courier can login')
    def test_courier_auth_without_login(self):
        data = {
            "password": password_creation(),
            "first_name": first_name_creation(),
            "login": login_creation
        }
        courier = requests.post(url=Constants.COURIER_REGISTRATION, data=data)
        response = requests.post(url=Constants.COURIER_LOGIN, data={"password": data.get("password")})
        assert "Недостаточно данных для входа" in response.text
        assert response.status_code == 400

    @allure.title('Courier cannot login without password')
    def test_courier_cannot_login_without_password(self):
        data = {
            "password": password_creation(),
            "first_name": first_name_creation(),
            "login": login_creation
        }
        courier = requests.post(url=Constants.COURIER_REGISTRATION, data=data)
        response = requests.post(url=Constants.COURIER_LOGIN, data={"login": data.get("login"),
                                                                    "password": ""})
        assert response.status_code == 400
        assert response.json().get("message") == 'Недостаточно данных для входа'

    @allure.title('Login attempt with wrong login or password')
    def test_courier_login_wrong_password(self):
        payload = {"login": 'wrong_login', "password": 'wrong_password'}
        response = requests.post(url=Constants.COURIER_LOGIN, data=payload)
        assert response.status_code == 404
        assert response.json().get("message") == 'Учетная запись не найдена'

