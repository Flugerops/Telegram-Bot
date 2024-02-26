from aiogram import Dispatcher, types, Router, F
from aiogram.enums import ParseMode
from ..misc import words
from ..keyboards import reply_keyboards, inline_keyboards


router = Router()



# ОБРОБНИК КНОПКИ ПОЧАТКОВІ СЛОВА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Початкові Слова'))
async def send_dict_start_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("start_words").items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)



# ОБРОБНИК КНОПКИ ПОДОРОЖ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Cлова На Тему Подорож'))
async def send_dict_trip_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("trip_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ ЇЖА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Їжа'))
async def send_dict_trip_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("food_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)

# ОБРОБНИК КНОПКИ КОЛЬОРИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Кольори'))
async def send_dict_colors_w(message: types.Message):
    from ..main import language
    formatted_dict = '\n'.join([f'{word} - {translation}\n' for word, translation in words.words.get(language).get("colors_words.").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ РОЗМОВА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Cлова На Тему Розмова'))
async def send_dict_conversation_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("conversation_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)
    

# ОБРОБНИК КНОПКИ ТВАРИНИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Тварини'))
async def send_dict_animals_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("animals_theme_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ АЙТІ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Айті'))
async def send_dict_it_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("it_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КОМАНДИ СПОРТ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Спорт'))
async def send_dict_sports_w(message: types.Message):
    from ..main import language 
    formatted_d = "\n".join([f'{word} - {translation}\n' for word, translation in words.words.get(language).get("sport_words").items()])
    await message.reply(formatted_d, ParseMode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ ШКОЛА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Школа'))
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("school_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)



# ОБРОБНИК КНОПКИ МУЗИКА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Музика'))  
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("music_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ КВАРТИРА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Квартира'))
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("house_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ РОБОТА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Робота'))
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("job_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ ФІЛЬМИ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Фільми'))
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.get(language).get("film_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ МОДА (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Мода'))
async def send_dict_school_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f"{word} - {translation}\n" for word, translation in words.words.get(language).get("fasion_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)


# ОБРОБНИК КНОПКИ ПИТАННЯ (ЗА ТЕМАМИ)
@router.message(F.text.contains('Слова На Тему Питання'))
async def send_dict_quest_w(message: types.Message):
    from ..main import language
    formatted_dict = "\n".join([f'{word} - {translation}\n' for word, translation in words.words.get(language).get("quest_words").items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_keyboards.exit_kb)