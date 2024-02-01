import asyncio
import logging
import sys

from aiogram.types import ReplyKeyboardRemove

import random
from aiogram import Bot, Dispatcher,F ,Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.methods import send_message
from aiogram.fsm.context import FSMContext



from .keyboards import reply_keyboards
from .utils.env import TOKEN
from .utils.states import Quiz
from .misc import words
from .handlers import words_themes_router, commands_router




dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!", reply_markup=reply_keyboards.language_kb)
    await message.answer("Я буду допомогати вивчати тобі різні мови", reply_markup=reply_keyboards.language_kb)
    await state.update_data(correct=0, incorrect=0)
    
@dp.message(lambda message: message.text == 'Англійська🇬🇧')
async def english(message: types.Message, state: FSMContext):
    await message.answer("Натисніть на опцію: ", reply_markup=reply_keyboards.user_mode_choice)


@dp.message(F.text == "Продовжити")
async def quiz(message: Message, state: FSMContext):

    random_word = random.choice(list(words.start_words.items()))
    await message.reply(f"Напишіть переклад слова: {random_word[0]}")    
    await state.update_data(translation=random_word)
    await state.set_state(Quiz.translation)
    


@dp.message(F.text == 'Вийти')
async def leave_quiz(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("incorrect") is None:
        await state.update_data(correct=0, incorrect=0)
        data = await state.get_data()
    print(data)
    correct = data.get("correct")
    incorrect = data.get("incorrect")
    await state.clear()
    
    if incorrect == 0:  
        await message.reply(f'Ви Не Помилялись В Цьому Квізі\nІ Отримали {correct} Правильних Відповідей!') 
    
    else:
        await message.reply(f"Ви Отримали {correct} Правильних Відповідей І {incorrect} Неправильних Відповідей.\nЦе {correct / (correct + incorrect) * 100}% Правильно.")
    await message.answer("Виберіть мод: ", reply_markup=reply_keyboards.user_mode_choice)


    

@dp.message(Quiz.translation)
async def check_translation(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("incorrect") is None:
        await state.update_data(correct=0, incorrect=0)
        data = await state.get_data()
    correct = data.get("correct")
    incorrect = data.get("incorrect")
    
    random_word = (await state.get_data()).get("translation")
    print(random_word)
    if message.text.casefold() == random_word[1].casefold():
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply("Ти відповів правильно.", reply_markup=reply_keyboards.start_quiz)
        correct += 1
    
    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply(f"Ти помилився, переклад: {random_word[1]}", reply_markup=reply_keyboards.start_quiz)
        incorrect += 1
    await state.update_data(correct=correct, incorrect=incorrect)
    
    

async def start() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(words_themes_router, commands_router)
    # And the run events dispatching
    await dp.start_polling(bot)
