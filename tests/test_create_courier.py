from data import Responses
from helpers.courier_data import CourierData 
import allure
import pytest


class TestCreateCourier:

    @allure.title("Позитивная проверка создания курьера")
    def test_create_courier (self, courier_service, auth_service, delete_courier_after_test):

        payload = CourierData.generate_payload()
        response = courier_service.create(payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_res = auth_service.login(payload["login"], payload["password"])
        courier_id = login_res.json().get("id")
        delete_courier_after_test.append(courier_id)

    @allure.title("Проверка ошибки при создании дубликата курьера")
    def test_create_duplicte_courier(self, courier_service, delete_courier_after_test, auth_service):
        
        payload, response1 = courier_service.create_random()
        assert response1.status_code == 201

        login_res = auth_service.login(payload["login"], payload["password"])
        delete_courier_after_test.append(login_res.json().get("id"))

        response2 = courier_service.create(payload)

        assert response2.status_code == 409
        assert response2.json()["message"] == Responses.LOGIN_ALREADY_USED

    @allure.title("Проверка создания курьера без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, courier_service, missing_field):

        valid_payload = CourierData.generate_payload()
        invalid_payload = valid_payload.copy()
        del invalid_payload[missing_field]

        response = courier_service.create(invalid_payload)

        assert response.status_code == 400           
        assert response.json()["message"] == Responses.NOT_ENOUGH_DATA