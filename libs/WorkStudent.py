import json

student_or_graduate_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Я студент, который ищет работу"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Я выпускник, который ищет работу"
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
student_or_graduate_keyboard = json.dumps(student_or_graduate_keyboard, ensure_ascii=False).encode('utf-8')
student_or_graduate_keyboard = str(student_or_graduate_keyboard.decode('utf-8'))

workstudent_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Ресурсы для поиска работы"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Чем может помочь Центр карьеры?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Вакансии"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Мероприятия Центра карьеры"
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
workstudent_keyboard = json.dumps(workstudent_keyboard, ensure_ascii=False).encode('utf-8')
workstudent_keyboard = str(workstudent_keyboard.decode('utf-8'))

workgraduate_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Опрос выпускника"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Карьерная консультация"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Как составить резюме"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Какие компании берут на работу?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Вакансии"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Что говорить на собеседовании?"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"8\"}",
                "label": "Предлагаю совместный проект с ЦК"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"8\"}",
                "label": "Главное меню"
            },
            "color": "default"
        }]
    ]
}
workgraduate_keyboard = json.dumps(workgraduate_keyboard, ensure_ascii=False).encode('utf-8')
workgraduate_keyboard = str(workgraduate_keyboard.decode('utf-8'))