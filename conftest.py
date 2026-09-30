import pytest
from helpers.api_client import ApiClient
from helpers.order_service import OrderService

@pytest.fixture
def api_client():
    return ApiClient() 


@pytest.fixture 
def order(): 
    return OrderService()