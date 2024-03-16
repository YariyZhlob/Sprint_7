import pytest
import random
import string
import requests
import allure
import constants


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
