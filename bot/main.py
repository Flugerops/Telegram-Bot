import asyncio

import logging

import sys
import requests
from os import getenv
from dotenv import load_dotenv

from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from aiogram.filters.callback_data import CallbackData


import random
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
from aiogram.methods import send_message
from aiogram.fsm.context import FSMContext
from .keyboards import reply_keyboards, inline_keyboards
from .utils.chatgpt import gpt
from .utils.env import TOKEN
from .utils.states import Quiz, Translate, Assistant, Language
from .utils import translation_router
from .misc import words
from .handlers import words_themes_router, commands_router



dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

language = None



@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Привіт, {hbold(message.from_user.full_name)}!")
    await message.answer("Я буду допомогати вивчати тобі різні мови!", reply_markup=reply_keyboards.language_kb)
    await state.update_data(correct=0, incorrect=0)
    await state.set_state(Language.language_select)





@dp.message(Language.language_select)
async def menu(message: Message, state: FSMContext):
    global language
    match message.text:
        case "Англійська🇬🇧":
            language = "eng"
        case "Французька🇫🇷":
            language = "french"

        case "Німецька🇩🇪":
            language = "ger"

        case "Іспанська🇪🇸":
            language = "spain"

        case "Італійська🇮🇹":
            language = "italy"

    await message.answer("Натисніть на опцію: ", reply_markup=reply_keyboards.user_mode_choice)
    await state.clear()



# @dp.message(F.text == "Французька🇫🇷" or F.text == "Англійська🇬🇧")
# async def language_select(message: Message):
#     global language
#     print(message.text)
#     match message.text:
#         case "Англійська🇬🇧":
#             language = "eng"
        
#         case "Французька🇫🇷":
#             language = "french"
    
# print(language)


@dp.message(F.text == "Продовжити")
async def quiz(message: Message, state: FSMContext):
    mode = (await state.get_data()).get("mod")
    print(mode)
    random_word=random.choice(list(words.words.get(language).get(mode).items()))
    await message.reply(f"Напишіть переклад слова: {random_word[0]}", reply_markup=reply_keyboards.quiz_menu)
    await state.update_data(translation=random_word)
    await state.set_state(Quiz.game)



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
        await message.reply(f'• Ви Не Помилялись В Цьому Квізі\n• І Отримали {correct} Правильних Відповідей!')
    elif correct == 0 and incorrect == 0:
        await message.reply(f'• Ти не відповідав в цьому квізі правильно')
    else:
        await message.reply(f"• Ви Отримали {correct} Правильних Відповідей\n•І {incorrect} Неправильних Відповідей.\n•Це {int(correct / (correct + incorrect) * 100)}% Правильно.")
    await message.answer("Виберіть мод: ", reply_markup=reply_keyboards.user_mode_choice)


@dp.callback_query(Quiz.check_mod)
async def select_mod_callback(callback_query: types.CallbackQuery, state: FSMContext):
    
    print(language)
    mode = callback_query.data
    print(mode)
    await callback_query.message.answer("Натисніть коли готові:", reply_markup=reply_keyboards.quiz_start)
    await state.update_data(mod=mode)
    await state.set_state(Quiz.game)


@dp.message(Quiz.game)
async def check_translation(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("incorrect") is None:
        await state.update_data(correct=0, incorrect=0)
        data = await state.get_data()
    correct = data.get("correct")
    incorrect = data.get("incorrect")
    print(data)
    random_word = (await state.get_data()).get("translation")
    print(random_word)
    if message.text.lower() in map(str.lower, random_word[1]):
        await message.react([ReactionTypeEmoji(emoji="👍")])
        await message.reply("Ти відповів правильно.", reply_markup=reply_keyboards.quiz_start)
        correct += 1
    
    elif F.text == "Я не можу відповісти":
        await message.reply(f"Переклад цього слова: {random_word[1]}", reply_markup=reply_keyboards.quiz_start)
        incorrect += 1
    
    else:
        await message.react([ReactionTypeEmoji(emoji="👎")])
        await message.reply(f"Ти помилився, переклад: {random_word[1]}", reply_markup=reply_keyboards.quiz_start)
        incorrect += 1
    await state.update_data(correct=correct, incorrect=incorrect)


@dp.message(Assistant.response)
async def generate_response(message: Message, state: FSMContext):        
    if message.text == "Повернутися в меню":   
        await message.answer("До побачення!", reply_markup=reply_keyboards.user_mode_choice)
        await state.clear()
    
    else:
        async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
            animate = await message.answer("Зачекайте")
            response = asyncio.create_task(gpt.generate_response(message.text))
            while True:
                await asyncio.sleep(1.5)
                animate = await animate.edit_text(animate.text + ".")         
                if response.done():
                    print(response)
                    break
            response = response.result()
            print(response) 
        try:
            await message.answer(response.get("response"), reply_markup=reply_keyboards.exit_kb)
        except:
            await message.answer("Вибачте, сталася помилка. Повторіть будь-ласка питання", reply_markup=reply_keyboards.exit_kb)
        await state.set_state(Assistant.response)


async def start() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    dp.include_router(translation_router)
    dp.include_routers(words_themes_router, commands_router)
    # And the run events dispatching
    await dp.start_polling(bot)
