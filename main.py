from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
import sys



import random
from aiogram import Bot, Dispatcher,F ,Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.methods import send_message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from data import words
import keyboard
from data import words


load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")


dp = Dispatcher()
router = Router()

class Quiz(StatesGroup):
    translation = State()



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


# async def quiz(message: Message, state: FSMContext):
#     random_word = random.choice(list(words.start_words.items()))
#     await message.reply(f"Напишіть переклад слова: {random_word[0]}")
#     async def echo(message: Message):          
#         if message.text.lower() == random_word[1]:
#             await message.reply("Ти відповів правильно.")
#         else:
#             await message.reply(f"Ти помилився, переклад: {random_word[1]}")
    

@dp.message(Quiz.translation)
async def check_translation(message: Message, state: FSMContext):
    random_word = (await state.get_data()).get("translation")
    print(random_word)
    if message.text.lower() == random_word[1]:
        await message.reply("Ти відповів правильно.")
    else:
        await message.reply(f"Ти помилився, переклад: {random_word[1]}")
    


@dp.message()
async def echo(message: Message, state: FSMContext):
    temp_msg = message.text.casefold()
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