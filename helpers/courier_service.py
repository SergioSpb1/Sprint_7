from data import MyUrls
from .api_client import ApiClient  
from .courier_data import CourierData  
import allure

class CourierService:
    def __init__(self, api_client: ApiClient):
        self.client = api_client
        self.base_url = MyUrls.MAIN_URL
        self.endpoint = MyUrls.CREATE_COURIER
        self.last_payload = None

    @allure.step("Создание курьера с указанными данными")
    def create(self, payload: dict):
      
        url = f"{self.base_url}{self.endpoint}"
        return self.client.post(url, json=payload)

    @allure.step("Создание курьера с рандомными данными")
    def create_random(self):
               
        payload = CourierData.generate_payload()
        response = self.create(payload)
        return payload, response 