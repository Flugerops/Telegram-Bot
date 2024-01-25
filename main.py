from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
import sys
import random
import openai

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.methods import send_message
from aiogram.fsm.storage.memory import MemoryStorage

from data import commands_list, words
import keyboard
from data import words

load_dotenv()
TOKEN = getenv("TOKEN")
CHAT_GPT_TOKEN = getenv("CHATGPT_TOKEN")
storage = MemoryStorage()

form_router = Router()


dp = Dispatcher(storage=storage)

class GPTFSM(StatesGroup):
    idle = State()
    
@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Hello i am Zmiini Novatory AI, just ask a question and i`l help you")
    await state.set_state(GPTFSM.idle)
    
@form_router.message(GPTFSM.idle)
async def response(message: Message, state: FSMContext):
    responce = await ai_answer(message.text)
    await message.answer(responce)
    await state.finish()

async def ai_answer(promt:str) -> str:
    answer = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":promt}]
    )
    return answer.choices[0].message.content

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())