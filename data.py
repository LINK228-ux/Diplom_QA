headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания нового заказа в системе
# содержат имя, фамилию, адрес заказчика, ближайшую к заказчику станцию метро, телефон заказчика,
# количество дней аренды,дату доставки,комментарий от заказчика, предпочитаемые цвета
order_body = {
    "firstName": "Kirill",
    "lastName": "Pokrovskiy",
    "address": "Dachnaya, 9",
    "metroStation": 6,
    "phone": "+7 800 555 35 35",
    "rentTime": 1,
    "deliveryDate": "2024-10-10",
    "comment": "None",
    "color": [
        "BLACK"
    ]
}

params_get = {
    "t": ""
}