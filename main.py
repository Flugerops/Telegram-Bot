from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
import sys
import random

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.methods import send_message

from data import commands_list, words
import keyboard
from data import words

load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!", reply_markup=keyboard.language_kb)
    await message.answer("Я буду допомогати вивчати тобі різні мови")
@dp.message(Command("language"))
async def choose_language(message: Message) -> None:
    await message.answer("Це мови які доступні для навчання: ", reply_markup=keyboard.language_kb)
@dp.message(Command("Англійська🇬🇧"))
async def english(message: Message) -> None:
    await message.answer("Натисніть на тему: ", reply_markup=keyboard.themes_kb)


# @dp.message(Command('allcommands'))
# async def all_commands_list(message:Message) -> None:
#     await message.answer(commands_list.english_functions)

# @dp.message(Command('startwords'))
# async def start_w(message: Message) -> None:
#     await message.answer(words.start_words)

# @dp.message(Command('random'))
# async def random_w(message: Message) -> None:
#     await message.answer(random.choice(words))

# @dp.message(Command('foodwords'))
# async def food_w(message: Message) -> None:
#     await message.answer(words.food_words)

# @dp.message(Command('tripwords'))
# async def trip_w(message: Message) -> None:
#     await message.answer(words.trip_words)

# @dp.message(Command('conversationwords'))
# async def conversation_w(message: Message) -> None:
#     await message.answer(words.conversation_words)

@dp.message()
async def echo(message: Message):
    temp_msg = message.text.lower()
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=keyboard.comm_kb)
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=keyboard.team_kb)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())