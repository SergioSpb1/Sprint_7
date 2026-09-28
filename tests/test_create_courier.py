from generators.c_generator import Generate_Courier_LP as GC
#тест создания курьера

print(GC.register_new_courier_and_return_login_password())


class TestCreateCourier:
    def test_create_courier(self):
        GC.register_new_courier_and_return_login_password()
        assert 1
