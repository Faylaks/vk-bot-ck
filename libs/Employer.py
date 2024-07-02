import json

employer_keyboard = {
     "one_time": False,
     "buttons": [
         [{
             "action": {
                 "type": "text",
                 "payload": "{\"button\": \"1\"}",
                 "label": "Мы уже взаимодействуем с СибГУТИ"
             },
             "color": "primary"
         }],
         [{
             "action": {
                 "type": "text",
                 "payload": "{\"button\": \"2\"}",
                 "label": "Мы не взаимодействуем с СибГУТИ"
             },
             "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
     ]
}

employer_keyboard = json.dumps(employer_keyboard, ensure_ascii=False).encode('utf-8')
employer_keyboard = str(employer_keyboard.decode('utf-8'))


interacts_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "План мероприятий на год"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Контакты"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Варианты сотрудничества"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Анонс вакансии/мероприятия"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Опрос работодателей"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}

interacts_keyboard = json.dumps(interacts_keyboard, ensure_ascii=False).encode('utf-8')
interacts_keyboard = str(interacts_keyboard.decode('utf-8'))


not_interacts_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Варианты сотрудничества"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "План мероприятий"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Как разместить вакансию"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Как разместить пост в соц сетях"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}

not_interacts_keyboard = json.dumps(not_interacts_keyboard, ensure_ascii=False).encode('utf-8')
not_interacts_keyboard = str(not_interacts_keyboard.decode('utf-8'))