import json

internship_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Где найти стажировку?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Что такое стажировка?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "После стажировки трудоустраивают?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
internship_keyboard = json.dumps(internship_keyboard, ensure_ascii=False).encode('utf-8')
internship_keyboard = str(internship_keyboard.decode('utf-8'))