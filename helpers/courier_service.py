from data import MyUrls
from .api_client import ApiClient  
from .courier_data import CourierData  
import allure

class CourierService:
    def __init__(self, api_client: ApiClient):
        self.client = api_client
          
    @allure.step("Создание курьера с указанными данными")
    def create(self, payload: dict):
      
        return self.client.post(MyUrls.COURIER_HANDLE, json=payload)

    @allure.step("Создание курьера с рандомными данными")
    def create_random(self):
               
        payload = CourierData.generate_payload()
        response = self.create(payload)
        return payload, response 

    @allure.step("Удаление курьера по ID") 
    def delete(self, courier_id: str): 
        
        url = f"{MyUrls.COURIER_HANDLE}/{courier_id}" 
        return self.client.delete(url)


