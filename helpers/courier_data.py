import random
import string
import allure

class CourierData:
    @staticmethod
    @allure.step ("Генерация рандомной строки")
    def generate_random_string(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    @allure.step ("Генерация рандомных данных курьера")
    def generate_payload(login: str = None, password: str = None, first_name: str = None) -> dict:

        if not login:
            login = CourierData.generate_random_string(10)
        if not password:
            password = CourierData.generate_random_string(10)
        if not first_name:
            first_name = CourierData.generate_random_string(10)

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }