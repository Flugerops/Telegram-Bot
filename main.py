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
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

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
    await message.answer("Я буду допомогати вивчати тобі різні мови", reply_markup=keyboard.language_kb)
@dp.message(lambda message: message.text == 'Англійська🇬🇧')
async def english(message: types.Message):
    await message.answer("Натисніть на опцію: ", reply_markup=keyboard.user_mode_choice)


@dp.message(lambda message: message.text == 'Почати квіз')
async def quiz(message: Message):
    random_word = random.choice(list(words.start_words.items()))
    await message.reply(f"Напишіть переклад слова: {random_word[0]}")
    async def echo(message: Message):          
        if message.text.lower() == random_word[1]:
            await message.reply("Ти відповів правильно.")
        else:
            await message.reply(f"Ти помилився, переклад: {random_word[1]}")
    
    # word = words.
    # await message.reply("")   

# @dp.message(Quiz.translation)
# async def check_translation(message: Message):
#     random_word = random.choice(list(words.start_words.items()))
#     await message.reply(f"Напишіть переклад слова: {random_word[0]}")
#     if message.text.lower() == random_word[1]:
#         await message.reply("Ти відповів правильно.")
#     else:
#         await message.reply(f"Ти помилився, переклад: {random_word[1]}")

 
# ОБРОБНИК КНОПКИ ПОЧАТКОВІ СЛОВА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Початкові Слова 💪')
async def send_dict_start_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.start_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN)



# ОБРОБНИК КНОПКИ ПОДОРОЖ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Cлова На Тему Подорож ✈️')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.trip_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ЇЖА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Їжа 🍌')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.food_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)

# ОБРОБНИК КНОПКИ КОЛЬОРИ
@dp.message(lambda message: message.text == 'Слова На Тему Кольори 🟣')
async def send_dict_colors_w(message: types.Message):
    formatted_dict = '\n'.join([f'{word} - {translation}' for word, translation in words.colors_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ РОЗМОВА
@dp.message(lambda message: message.text == 'Cлова На Тему Розмова 🗣')
async def send_dict_conversation_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.conversation_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)
    

# ОБРОБНИК КНОПКИ ТВАРИНИ
@dp.message(lambda message: message.text == 'Слова На Тему Тварини 🐍')
async def send_dict_animals_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.animals_theme_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ АЙТІ
@dp.message(lambda message: message.text == 'Слова На Тему Айті 💻')
async def send_dict_it_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.it_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КОМАНДИ СПОРТ
@dp.message(lambda message: message.text == 'Слова На Тему Спорт ⚽️')
async def send_dict_sport_w(message: types.Message):
    formatted_dict = "\n".join([f'{words} - {translation}' for word, translation in words.sport_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ШКОЛА 
@dp.message(lambda message: message.text == 'Слова На Тему Школа 🏫')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.school_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)



# ОБРОБНИК КНОПКИ МУЗИКА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Музика🎵')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.music_word.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


@dp.message()
async def echo(message: Message):
    temp_msg = message.text.lower()
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=keyboard.comm_kb)
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=keyboard.team_kb)
    if temp_msg == "слова по темам":
        await message.answer("Виберіть тему:",reply_markup=keyboard.themes_kb)
    if temp_msg == "вгадай переклад слова":
        await message.answer("Натисніть коли готові:",reply_markup=keyboard.start_quiz)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())