from data import MyUrls
from helpers.api_client import ApiClient
import allure

class AuthService:
    def __init__(self, api_client: ApiClient):
        self.client = api_client
        self.base_url = MyUrls.MAIN_URL
        self.endpoint = MyUrls.LOGIN_COURIER

    @allure.step ("Авторизация - вызов метода POST с логином и паролем")
    def login(self, login: str, password: str):
        payload = {
            "login": login,
            "password": password
        }
        url = f"{self.base_url}{self.endpoint}"
        return self.client.post(url, json=payload)