import requests
import aiohttp
from ..utils.env import X_RapidAPI_Key



class ChatGPT:
    def __init__(self) -> None:
        self.api_key = X_RapidAPI_Key
        self.url = "https://chatgpt-openai1.p.rapidapi.com/ask"
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "open-ai-chatgpt.p.rapidapi.com"}


    async def generate_response(self, message):
        payload = { "query": message }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload, headers=self.headers) as response:
                try:
                    
                    data = await response.json()
                    text = await response.text()
                    print(data, text, response.url, response.headers)
                    return data
                except:
                    print(response.url, await response.text())


gpt = ChatGPT()