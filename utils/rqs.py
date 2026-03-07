import requests
import json

API = "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"


url = "https://openrouter.ai/api/v1/chat/completions"


headers = {"Authorization": f"Bearer {API}"}

payload = {
    "model": "google/gemma-3n-e2b-it:free",
    "messages": [{"role": "user", "content": "{promt}"}],
}
