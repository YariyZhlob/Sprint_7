import pytest
import random
import string
import requests
import allure
import constants


@pytest.fixture()
def create_courier():
    def generate_new_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_new_random_string(10)
    password = generate_new_random_string(10)
    first_name = generate_new_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    return response


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("Login creation")
def login_creation():
    login = generate_random_string(10)
    return login


@allure.step("Password creation")
def password_creation():
    password = generate_random_string(10)
    return password


@allure.step("First name creation")
def first_name_creation():
    first_name = generate_random_string(10)
    return first_name


@allure.step("Create payload")
def create_payload():
    payload = {"login": login_creation,
               "password": password_creation,
               "first_name": first_name_creation}
    return payload


@allure.step("Create payload")
def create_courier_payload_with_known_params(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


# @allure.step('Создаем заказ')
# def create_order(color):
#     InformationForOrder.info_for_order["color"] = color
#     payload = InformationForOrder.info_for_order
#     response = requests.post(Url.URL_ORDER_LIST, data=json.dumps(payload))
#     return response.json()
#
#
# @allure.step('Order creation')
# def order_creation(payload):
#     response = requests.post(url=constants.CREATE_ORDER, data=json.dumps(payload))
#     return response.json()
