import allure

class TestOrdersList:

    @allure.title("Получение списка заказов конкретного курьера")
    def test_get_orders_list_by_courier_id(self, courier_lifecycle, order_service):
        
        courier_id = courier_lifecycle["id"]

        response = order_service.get_list_by_courier(courier_id)

        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert response_json["orders"] == []
