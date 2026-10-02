import pytest
import allure
from data import MyUrls, Responses

class TestLoginCourier:

    @allure.title("Позитивная проверка логина курьера")
    def test_login_courier(self, auth_service, courier_lifecycle):
        
        login = courier_lifecycle["login"]
        password = courier_lifecycle["password"]

        response = auth_service.login(login=login, password=password)

        assert response.status_code == 200 
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Авторизация с неверным паролем")
    def test_wrong_password(self, auth_service, courier_lifecycle):

        correct_login = courier_lifecycle["login"]
        inv_p = "bad_password12"

        response = auth_service.login(correct_login, inv_p)

        assert response.status_code == 404
        assert response.json()["message"] == Responses.ACCOUNT_NOT_FOUND

    @allure.title("Авторизация с неверным логином")   
    def test_wrong_login(self, auth_service, courier_lifecycle):

        inv_login = "incorrect7"
        corr_password = courier_lifecycle["password"]

        response = auth_service.login(inv_login, corr_password)

        assert response.status_code == 404
        assert response.json()["message"] == Responses.ACCOUNT_NOT_FOUND

    @pytest.mark.parametrize("missing_field, expected_status", [
        ("login", 400), 
        pytest.param("password", 504, marks=pytest.mark.xfail(reason="Ошибка 504 при отсутствии пароля, согласно документации ожидаем 400")) 
    ])
    @allure.title("Авторизация без обязательного поля") 
    def test_missing_field(self, api_client, missing_field, expected_status, courier_lifecycle):

        broken_payload = {
            "login": courier_lifecycle["login"],
            "password": courier_lifecycle["password"]
        }
        del broken_payload[missing_field]

        response = api_client.post(MyUrls.LOGIN_COURIER, broken_payload)

        assert response.status_code == expected_status
