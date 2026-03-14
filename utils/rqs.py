import requests
import json
from datetime import time, timedelta, datetime

API = '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'


def get(url: str, headers: dict | None = None, payload: dict | None = None) -> tuple:
    response = requests.get(url, headers=headers, data=json.dumps(payload))
    return (response.text, response.status_code)


def post(url: str, headers: dict | None = None, data: dict | None = None):
    response = requests.post(url, headers=headers, json=data)
    return response


url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API}"
}

payload = {
    "model": "stepfun/step-3.5-flash:free",
    "messages": [{"role": "user", "content": '{promt}'}]
}


class History:
    def __init__(self) -> None:
        self.promt = ''
        self.history = ''
        self.expire = datetime.now() + timedelta(minutes=30)
        self.main_promt = 'История диалога:\n{history}\n\nТекущее обращение: {promt}\n\nОтветь на текущее обращение, используя историю для контекста, если она есть.'

    def format_message_with_history(self, promt):
        self.promt = promt
        if self.history:
            return self.main_promt.format(promt=promt, history=self.history)
        else:
            return self.main_promt.format(promt=promt, history='История пуста, это первое обращение.')

    def add_history(self, arsen):
        self.history += 'Твой ответ: ' + arsen + '\nМой вопрос: ' + self.promt + '\n\n'


def send_request(promt: str) -> str:
    payload['messages'][0]['content'] = promt
    response = post(url, headers, payload)
    data = response.json()
    try:
        choices = data.get("choices", [])
        message = choices[0].get("message", {})
        content = message.get("content", "")
    except Exception as e:
        raise Exception(data)
    return content


# history = History()
# message = history.format_message_with_history('Привет, напиши 1')

# answer = send_request(message)
# print(answer)

# history.add_history(answer)



expire = datetime.now() + timedelta(minutes=-30)

if expire < datetime.now():
    print("ПРАВДА")
