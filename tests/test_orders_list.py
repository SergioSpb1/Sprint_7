from helpers.order_service import OrderService
import allure



class TestCouriersOrders:

    @allure.title("Получение списка заказов курьера")
    def test_login_courier(self):
   
        s = OrderService()
        response = s.get_list_no_param()
        json_data = response.json()
        
        assert response.status_code == 200
        assert 'orders' in json_data
        assert isinstance(json_data, dict)
           
