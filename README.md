# Diplom_2

# Failed tests:
TestCreateOrder:

* test_create_order_without_authorization

Не совпадают код и тело ответа 

ОР: код ответа 401, тело ответа - {"success": False, "message": "You should be authorised"}'

ФР: код ответа 200, тело ответа - {"success": true,"name": "...",
    "order": {
        "number": ...
    }
}

