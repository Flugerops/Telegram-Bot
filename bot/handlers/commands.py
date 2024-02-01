from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from ..misc import words
from ..keyboards import reply_keyboards


router = Router()


@router.message()
async def echo(message: types.Message):
    temp_msg = message.text.casefold()
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=reply_keyboards.comm_kb)
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=reply_keyboards.team_kb)
    if temp_msg == "слова по темам":
        await message.answer("Виберіть тему:",reply_markup=reply_keyboards.themes_kb)
    if temp_msg == "вгадай переклад слова":
        await message.answer("Натисніть коли готові:",reply_markup=reply_keyboards.start_quiz)
        
@router.callback_query()
async def callback_query_keyboard(callback_query: types.CallbackQuery,):
    if callback_query.data == "exit":
        await callback_query.message.answer("Виберіть мод:", reply_markup=reply_keyboards.user_mode_choice)

