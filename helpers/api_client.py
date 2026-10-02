import requests
import allure

class ApiClient:
    def __init__(self):
        pass

    @allure.step("Вызов метода post")
    def post(self, url: str, json: dict = None):
        return requests.post(url, json=json)

    @allure.step("Вызов метода delete")
    def delete(self, url: str):
        return requests.delete(url)

