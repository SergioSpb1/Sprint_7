class MyUrls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    ORDERS_HANDLE = '/api/v1/orders'
    
class Responses:
# Согласно переписке qa-fs-python_study_M6 в телемосте 25.09.2026: 
# "подстраиваться под документацию тут не нужно: ориентируйся на то, что сервис реально возвращает, тогда прогон станет зелёным."
# в ассерт подставлен реальный ответ сервера при попытке создания дубля, тест passed.
# При проверке на значение из документации тест failed
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

class OrderPayload:
    ORDER1 = {
            "firstName": "Sergio",
            "lastName": "Avs",
            "address": "Spb, Nevski 1",
            "metroStation": 1,
            "phone": "+7 812 111 22 33",
            "rentTime": 5,
            "deliveryDate": "20270-01-04",
            "comment": "Test order"
        }

