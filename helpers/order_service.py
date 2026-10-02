import requests
import allure
from data import MyUrls

class OrderService:
    def __init__(self):
        self.session = requests.Session()

    @allure.step("POST на создание заказа")
    def create(self, order_data: dict):
        return self.session.post(MyUrls.ORDERS_HANDLE, json=order_data)

    @allure.step("GET на получение списка заказов курьера")
    def get_list_by_courier(self, courier_id):
        url = f"{MyUrls.ORDERS_HANDLE}?courierId={courier_id}"
        return self.session.get(url)

