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


# ОБРОБНИК КНОПКИ ПОЧАТКОВІ СЛОВА
@dp.message(lambda message: message.text == 'Початкові слова 💪')
async def send_dict_start_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.start_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ПОДОРОЖ
@dp.message(lambda message: message.text == 'Cлова На Тему Подорож ✈️')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.trip_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ЇЖА
@dp.message(lambda message: message.text == 'Слова На Тему Їжа 🍌')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.food_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN)


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