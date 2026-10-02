import pytest
from helpers.api_client import ApiClient
from helpers.courier_service import CourierService
from helpers.auth_service import AuthService
from helpers.order_service import OrderService

@pytest.fixture
def courier_lifecycle(courier_service, auth_service):
 
    payload, _ = courier_service.create_random()
    
    login_res = auth_service.login(payload["login"], payload["password"])
    courier_id = login_res.json().get("id")

    yield {
        "id": courier_id,
        "login": payload["login"],
        "password": payload["password"]
    }

    if courier_id:
        courier_service.delete(courier_id)


@pytest.fixture
def delete_courier_after_test(courier_service):

    couriers_to_delete = []

    yield couriers_to_delete

    for courier_id in couriers_to_delete:
        if courier_id:
            courier_service.delete(courier_id)

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

@pytest.fixture(scope="session")
def courier_service(api_client):
    return CourierService(api_client)

@pytest.fixture(scope="session")
def auth_service(api_client):
    return AuthService(api_client)

@pytest.fixture(scope="session")
def order_service():
    return OrderService()