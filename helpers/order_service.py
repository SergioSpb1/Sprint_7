import requests
from data import MyUrls

class OrderService:
    def __init__(self):
        self.session = requests.Session()

    def create(self, order_data: dict):
        url = f"{MyUrls.MAIN_URL}{MyUrls.ORDERS_HANDLE}"
        return self.session.post(url, json=order_data)

    def get_list_no_param(self):
        url = f"{MyUrls.MAIN_URL}{MyUrls.ORDERS_HANDLE}"
        return self.session.get(url)

