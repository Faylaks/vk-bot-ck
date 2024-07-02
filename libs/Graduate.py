import json

# Кнопки клавиатуры для выпускника с кнопкой "Назад"
graduate_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Когда встреча выпускников?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Поделюсь своей карьерной историей"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Есть предложение для сотрудничества"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Опрос выпускников"
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


graduate_keyboard = json.dumps(graduate_keyboard, ensure_ascii=False).encode('utf-8')
graduate_keyboard = str(graduate_keyboard.decode('utf-8'))