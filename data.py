headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания нового заказа в системе
# содержат имя, фамилию, адрес заказчика, ближайшую к заказчику станцию метро, телефон заказчика,
# количество дней аренды,дату доставки,комментарий от заказчика, предпочитаемые цвета
order_body = {
    "firstName": "Oleg",
    "lastName": "Mishkin",
    "address": "Leninna, 6",
    "metroStation": 6,
    "phone": "+7 912 15 32 193",
    "rentTime": 1,
    "deliveryDate": "2024-06-19",
    "comment": "None",
    "color": [
        "WHITE"
    ]
}

params_get = {
    "t": ""
}
