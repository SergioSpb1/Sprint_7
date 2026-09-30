import pytest
import allure
from data import OrderPayload as OP

class TestCreateOrder:

    @pytest.mark.parametrize("color_payload, colors_desc", [
        (["BLACK"], "only BLACK"),
        (["GREY"], "only GREY"),
        (["BLACK", "GREY"], "both colors"),
        ([], "no colors"),
        (None, "no color field")
    ])
    @allure.title("Создание заказа с цветами: {colors_desc}")
    def test_create_order(self, order, color_payload, colors_desc):
        
        order_payload = OP.ORDER1

        if color_payload is not None:
            order_payload["color"] = color_payload

        response = order.create(order_payload)

        assert response.status_code == 201
        response_json = response.json()
        assert "track" in response_json
        assert isinstance(response_json["track"], int)