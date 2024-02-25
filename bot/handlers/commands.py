from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from ..misc import words
from ..keyboards import reply_keyboards, inline_keyboards
from ..utils import states
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendContact
from ..utils.states import Language

router = Router()




@router.message()
async def echo(message: types.Message, state: FSMContext):
    temp_msg = message.text.casefold()
    
    if temp_msg == "контакти розробників":
        # await message.answer("Zmiini_Novatori", reply_markup = inline_keyboards.team_kb)
        await message.answer_contact(phone_number="+380980195811", first_name="Тім лід")
        await message.answer_contact(phone_number="+380976938192", first_name="Бек енд")
        await message.answer_contact(phone_number="+380663831117", first_name="Фронт енд")
    
    if temp_msg == "слова по темам":
        await message.answer("Виберіть тему:",reply_markup= reply_keyboards.themes_kb)
    
    if temp_msg == "вгадай переклад слова":
        await message.answer("Виберіть режим:",reply_markup= inline_keyboards.inline_themes)
        await state.set_state(states.Quiz.check_mod)
    
    
    if temp_msg == "перекладач":
        from ..main import language
        if language == "eng":
            await message.answer("Виберіть режим:", reply_markup= inline_keyboards.eng_translator_kb)
        
        elif language == "french":
            await message.answer("Виберіть режим:", reply_markup= inline_keyboards.fr_translator_kb)

        await state.set_state(states.Translate.message_check)

    if temp_msg == "асистент":
        await message.answer("Привіт, я асистент команди 'Зміїні Новатори', я допоможу вам з вивченням мов. Задавайте ваше питання:")
        await state.set_state(states.Assistant.response)


    if temp_msg == 'вибір мови':
        await message.answer("Виберіть мову: ", reply_markup=reply_keyboards.language_kb)
        await state.set_state(Language.language_select)
        
        

@router.callback_query()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == "exit":
        await callback_query.message.answer("Виберіть мод:", reply_markup=reply_keyboards.user_mode_choice)

