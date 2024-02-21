import requests
import aiohttp
from ..utils.env import X_RapidAPI_Key

class ChatGPT:
    def __init__(self) -> None:
        self.api_key = X_RapidAPI_Key
        self.url = "https://chat-gpt-3-5-turbo.p.rapidapi.com/ChatComplitition"
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "chat-gpt-3-5-turbo.p.rapidapi.com"}

    async def generate_response(self, message):
        payload = {"Body": {
            "messages": [
                {
                    "role": "assistant",
                    "content": "Твоє ім`я бот зміїних новаторів, ти розмовляєш Українською мовою і допомагаєш користувачам вивчати мови, ти потрібен відповідати тільки на питання які стосуются вивчення мов!!"
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "temperature": 0.9,
		    "max_tokens": 500,
            "stream": False
        }}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload, headers=self.headers) as response:
                print(response.url)
                return await response.json()
    
gpt = ChatGPT()

