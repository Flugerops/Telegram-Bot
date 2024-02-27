from aiogram import Dispatcher, types, Router, F
from aiogram.filters.callback_data import CallbackData
from .states import Translate
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from translators import translate_text
from ..keyboards import reply_keyboards, inline_keyboards


router = Router()

@router.callback_query(Translate.message_check)
async def check_message(callback_query: types.CallbackQuery, state: FSMContext):
    mode = callback_query.data
    await callback_query.message.reply("Напишіть текст:")
    await state.update_data(mod=mode)
    await state.set_state(Translate.translation)

@router.message(Translate.translation)
async def translation(message: Message, state: FSMContext):
    from ..main import language
    mode = (await state.get_data()).get("mod")

    if message.text == "❌":
        await state.clear()
        await message.answer("Виберіть мод: ", reply_markup=reply_keyboards.user_mode_choice)

    elif message.text == "🔄️":
        await state.clear()
        if language == "eng":
            await message.answer("Виберіть режим:", reply_markup=inline_keyboards.eng_translator_kb)
        
        elif language == "french":
            await message.answer("Виберіть режим:", reply_markup=inline_keyboards.fr_translator_kb)
            await state.set_state(Translate.message_check)

        elif language == "ger":
            await message.answer('Виберіть режим: ', reply_markup=inline_keyboards.gr_translator_kb)
            await state.set_state(Translate.message_check)

        elif language == "spain":
            await message.answer('Виберіть режим: ', reply_markup=inline_keyboards.sp_translator_kb)
            await state.set_state(Translate.message_check)

        elif language == "italy":
            await message.answer('Виберіть режим: ', reply_markup= inline_keyboards.it_translator_kb)
            await state.set_state(Translate.message_check)



    elif mode == "en_to_ua":
        await message.reply("Переклад з фнглійської на українську мову: ")
        await message.answer(translate_text(message.text, translator="google", from_language="en", to_language='uk'), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == "ua_to_en":
        await message.reply('Переклад з української на англійську мову: ')
        await message.answer(translate_text(message.text, translator="google", from_languag="uk", to_language='en'), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == "fr_to_ua":
        await message.reply("Переклад з французької на українську мову: ")
        await message.answer(translate_text(message.text, translator="google", from_languag="fr", to_language='uk'), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == "ua_to_fr":
        await message.reply('Переклад з української на французську мову: ')
        await message.answer(translate_text(message.text, translator="google", from_languag="uk", to_language='fr'), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == "gr_to_ua":
        await message.reply('Переклад з німецької на українську: ')
        await message.reply(translate_text(message.text, translator="google", from_languag="de", to_language='uk'), reply_markup=reply_keyboards.translator_menu_kb)
    

    elif mode == "ua_to_gr":
        await message.reply('Переклад з української на німецьку: ')
        await message.reply(translate_text(message.text, translator="google", from_languag="uk", to_language='de'), reply_markup=reply_keyboards.translator_menu_kb)

        
    elif mode == "sp_to_ua":
        await message.reply('Переклад з іспанської на українську: ')
        await message.reply(translate_text(message.text, translator="google", from_language="es", to_language="uk"), reply_markup=reply_keyboards.translator_menu_kb)

    elif mode == "ua_to_sp":
        await message.reply('Переклад з української на іспанську: ')
        await message.reply(translate_text(message.text, translator="google", from_language="uk", to_language="es"), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == "it_to_ua":
        await message.reply('Переклад з італійської на українську: ')
        await message.reply(translate_text(message.text, translator = "google", from_language="it", to_language="uk"), reply_markup=reply_keyboards.translator_menu_kb)


    elif mode == 'ua_to_it':
        await message.reply('Переклад з української на італійську: ')
        await message.reply(translate_text(message.text, translator="google", from_language="uk", to_language="it"), reply_markup=reply_keyboards.translator_menu_kb)


    await message.answer("Виберіть опцію: ", reply_keyboards.translator_menu_kb)
    await state.clear()