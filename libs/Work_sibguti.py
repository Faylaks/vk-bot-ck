import json

# Кнопки клавиатуры для сотрудника СибГУТИ
sibguti_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Ищу сотрудника среди студентов"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Ищу сотрудника среди выпускников"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Приглашаю компанию на мероприятие"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Задача для практики студентам"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Предлагаю компанию для практики"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Мероприятия Центра карьеры"
            },
            "color": "primary"
        }],
        [{
            "action":{
                "type": "text",
                "payload": "{\"button\": \"7\"}",
                "label": "Я руководитель по практике"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"back\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}

# Преобразование клавиатуры в JSON-формат
sibguti_keyboard = json.dumps(sibguti_keyboard, ensure_ascii=False).encode('utf-8')
sibguti_keyboard = str(sibguti_keyboard.decode('utf-8'))