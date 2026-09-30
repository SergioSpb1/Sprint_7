from data import Responses
from helpers.courier_service import CourierService as CS
from helpers.courier_data import CourierData 
import allure
import pytest


class TestCreateCourier:

    @allure.title("Позитивная проверка создания курьера")
    def test_create_courier(self, api_client):
        courier = CS(api_client)
        _, responce = courier.create_random()
                
        assert responce.status_code == 201
        assert responce.json() == {"ok": True}

    @allure.title("Проверка ошибки при создании дубликата курьера")
    def test_create_duplicte_courier(self, api_client):
        courier = CS(api_client)

        first_payload, response1 = courier.create_random()
        assert response1.status_code == 201
        
        response2 = courier.create(first_payload)

        assert response2.status_code == 409
        assert response2.json()["message"] == Responses.LOGIN_ALREADY_USED

    @allure.title("Проверка создания курьера без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, api_client, missing_field):

        service = CS(api_client)
       
        valid_payload = CourierData.generate_payload()
        invalid_payload = valid_payload.copy()
        del invalid_payload[missing_field]

        response = service.create(invalid_payload)

        assert response.status_code == 400           
        assert response.json()["message"] == Responses.NOT_ENOUGH_DATA

        



    
