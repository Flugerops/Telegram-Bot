import asyncio
import logging
import sys

from aiogram.types import ReplyKeyboardRemove

import random
from aiogram import Bot, Dispatcher,F ,Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.methods import send_message
from aiogram.fsm.context import FSMContext

from .keyboards import keyboard
from .utils.env import TOKEN
from .utils.states import Quiz
from .misc import words
from .handlers import words_themes_router, commands_router




dp = Dispatcher()

correct = 0
incorrect = 0

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!", reply_markup=keyboard.language_kb)
    await message.answer("Я буду допомогати вивчати тобі різні мови", reply_markup=keyboard.language_kb)
@dp.message(lambda message: message.text == 'Англійська🇬🇧')
async def english(message: types.Message):
    await message.answer("Натисніть на опцію: ", reply_markup=keyboard.user_mode_choice)


@dp.message(lambda message: message.text == 'Почати квіз')
async def quiz(message: Message, state: FSMContext):

    random_word = random.choice(list(words.start_words.items()))
    await message.reply(f"Напишіть переклад слова: {random_word[0]}")    
    await state.update_data(translation=random_word)
    await state.set_state(Quiz.translation)  

@dp.message(F.text == 'Вийти')
async def leave_quiz(message: Message, state: FSMContext):
    await state.clear()
    # await message.reply(f"Ви отримали {correct} правильних відповідей і {incorrect} неправильних відповідей.\n Це {correct / incorrect}% правильно.")
    await message.answer("Виберіть мод: ", reply_markup=keyboard.user_mode_choice)



@dp.message(Quiz.translation)
async def check_translation(message: Message, state: FSMContext):
    random_word = (await state.get_data()).get("translation")
    global correct
    global incorrect
    print(random_word)
    if message.text.casefold() == random_word[1]:
        await message.reply("Ти відповів правильно.")
        correct += 1
    else:
        await message.reply(f"Ти помилився, переклад: {random_word[1]}")
        incorrect += 1
    


async def start() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(words_themes_router, commands_router)
    # And the run events dispatching
    await dp.start_polling(bot)
