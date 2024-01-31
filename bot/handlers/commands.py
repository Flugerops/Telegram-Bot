from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from ..misc import words
from ..keyboards import keyboard

router = Router()


@router.message()
async def echo(message: types.Message):
    print(echo)
    temp_msg = message.text.casefold()
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=keyboard.comm_kb)
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=keyboard.team_kb)
    if temp_msg == "слова по темам":
        await message.answer("Виберіть тему:",reply_markup=keyboard.themes_kb)
    if temp_msg == "вгадай переклад слова":
        await message.answer("Натисніть коли готові:",reply_markup=keyboard.start_quiz)