import requests
import json

API = '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'


def get(url: str, headers: dict | None = None, payload: dict | None = None) -> tuple:
    response = requests.get(url, headers=headers, data=json.dumps(payload))
    return (response.text, response.status_code)


def post(url: str, headers: dict | None = None, data: dict | None = None) -> tuple:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response


url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API}"
}

payload = {
    "model": "stepfun/step-3.5-flash:free",
    "messages": [{"role": "user", "content": '{promt}'}]
}


def send_request(promt: str) -> str:
    response = post(url, headers, payload['messages'][0]['content'].format(promt=promt))
    data = response.json()
    print(data)
    choices = data.get("choices", [])
    message = choices[0].get("message", {})
    content = message.get("content", "")
    return content