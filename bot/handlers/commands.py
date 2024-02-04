from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from ..misc import words
from ..keyboards import reply_keyboards, inline_keyboards
from ..utils import states
from aiogram.fsm.context import FSMContext

router = Router()


@router.message()
async def echo(message: types.Message, state: FSMContext):
    temp_msg = message.text.casefold()
    
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=reply_keyboards.comm_kb)
    
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=reply_keyboards.team_kb)
    
    if temp_msg == "слова по темам":
        await message.answer("Виберіть тему:",reply_markup=reply_keyboards.themes_kb)
    
    if temp_msg == "вгадай переклад слова":
        await message.answer("Виберіть режим:",reply_markup = inline_keyboards.inline_themes)
        await state.set_state(states.Quiz.check_mod)
        
        
@router.callback_query()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == "exit":
        await callback_query.message.answer("Виберіть мод:", reply_markup=reply_keyboards.user_mode_choice)

