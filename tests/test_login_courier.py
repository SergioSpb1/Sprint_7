from data import MyUrls, Responses
from helpers.courier_service import CourierService as CS
from helpers.auth_service import AuthService
import allure
import pytest


class TestLoginCourier:

    @allure.title("Позитивная проверка логина курьера")
    def test_login_courier(self, api_client):
        auth = AuthService(api_client)

        new_courier = CS(api_client)
        payload, _ = new_courier.create_random()

        response = auth.login(login=payload["login"], password=payload["password"])

        assert response.status_code == 200 
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Авторизация с неверным паролем")
    def test_wrong_password(self, api_client):
        auth = AuthService(api_client)
        new_courier = CS(api_client)
        
        valid_payload, _ = new_courier.create_random()

        correct_login = valid_payload["login"]
        inv_p = "bad_password12"

        response = auth.login(correct_login,inv_p)

        assert response.status_code == 404
        assert response.json()["message"] == Responses.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация с неверным логином")   
    def test_wrong_login(self, api_client):
        auth = AuthService(api_client)
        new_courier = CS(api_client)
        
        valid_payload, _ = new_courier.create_random()

        inv_login = "incorrect7"
        corr_password = valid_payload["password"]

        response = auth.login(inv_login, corr_password)

        assert response.status_code == 404
        assert response.json()["message"] == Responses.ACCOUNT_NOT_FOUND

    @pytest.mark.parametrize("missing_field, expected_status", [("login", 400), pytest.param( "password", 504, marks=pytest.mark.xfail(reason="Ошибка 504 при отсутствии пароля, согласно документации ожидаем 400") ) ])
    @allure.title("Авторизация без обязательного поля") 
    def test_missing_field(self, api_client, missing_field, expected_status):
        new_courier = CS(api_client)
        
        valid_payload, _ = new_courier.create_random()
        broken_payload = valid_payload.copy() 
        del broken_payload[missing_field]

        url = f'{MyUrls.MAIN_URL}{MyUrls.LOGIN_COURIER}'
        response = api_client.post(url, broken_payload)

        assert response.status_code == 400
