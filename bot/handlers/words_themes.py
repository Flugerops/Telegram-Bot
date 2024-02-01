from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from ..misc import words
from ..keyboards import keyboard

router = Router()




# ОБРОБНИК КНОПКИ ПОЧАТКОВІ СЛОВА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Початкові Слова'))
async def send_dict_start_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.start_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)



# ОБРОБНИК КНОПКИ ПОДОРОЖ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Cлова На Тему Подорож'))
async def send_dict_trip_w(message: types.Message):
    print("Тута")
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.trip_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ ЇЖА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Їжа'))
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.food_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)

# ОБРОБНИК КНОПКИ КОЛЬОРИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Кольори'))
async def send_dict_colors_w(message: types.Message):
    formatted_dict = '\n'.join([f'{word} - {translation}' for word, translation in words.colors_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ РОЗМОВА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Cлова На Тему Розмова'))
async def send_dict_conversation_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.conversation_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)
    

# ОБРОБНИК КНОПКИ ТВАРИНИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Тварини'))
async def send_dict_animals_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.animals_theme_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ АЙТІ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Айті'))
async def send_dict_it_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.it_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КОМАНДИ СПОРТ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Спорт'))
async def send_dict_sport_w(message: types.Message):
    formatted_dict = "\n".join([f'{words} - {translation}' for word, translation in words.sport_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ ШКОЛА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Школа'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.school_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)



# ОБРОБНИК КНОПКИ МУЗИКА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Музика'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.music_word.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ КВАРТИРА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Музика'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.house_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ РОБОТА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Робота'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ ФІЛЬМИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Фільми'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)


# ОБРОБНИК КНОПКИ МОДА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Мода'))
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard.exit_kb)

