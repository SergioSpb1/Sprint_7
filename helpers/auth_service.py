from data import MyUrls
from helpers.api_client import ApiClient
import allure

class AuthService:
    def __init__(self, api_client: ApiClient):
        self.client = api_client

    @allure.step ("Авторизация - вызов метода POST с логином и паролем")
    def login(self, login: str, password: str):
        payload = {
            "login": login,
            "password": password
        }
        return self.client.post(MyUrls.LOGIN_COURIER, json=payload)