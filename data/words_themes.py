from main import dp, types, ParseMode
import words



# ОБРОБНИК КНОПКИ ПОЧАТКОВІ СЛОВА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Початкові Слова 💪')
async def send_dict_start_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.start_words.items()])
    await message.answer(formatted_dict, parse_mode=ParseMode.MARKDOWN)



# ОБРОБНИК КНОПКИ ПОДОРОЖ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Cлова На Тему Подорож ✈️')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.trip_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ЇЖА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Їжа 🍌')
async def send_dict_trip_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.food_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)

# ОБРОБНИК КНОПКИ КОЛЬОРИ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Кольори 🟣')
async def send_dict_colors_w(message: types.Message):
    formatted_dict = '\n'.join([f'{word} - {translation}' for word, translation in words.colors_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ РОЗМОВА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Cлова На Тему Розмова 🗣')
async def send_dict_conversation_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.conversation_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)
    

# ОБРОБНИК КНОПКИ ТВАРИНИ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Тварини 🐍')
async def send_dict_animals_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.animals_theme_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ АЙТІ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Айті 💻')
async def send_dict_it_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.it_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КОМАНДИ СПОРТ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Спорт ⚽️')
async def send_dict_sport_w(message: types.Message):
    formatted_dict = "\n".join([f'{words} - {translation}' for word, translation in words.sport_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ШКОЛА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Школа 🏫')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.school_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)



# ОБРОБНИК КНОПКИ МУЗИКА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Музика🎵')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.music_word.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ КВАРТИРА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Музика🎵')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.house_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ РОБОТА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Робота 💼')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ ФІЛЬМИ (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Фільми 🎬')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)


# ОБРОБНИК КНОПКИ МОДА (ЗА ТЕМАМИ)
@dp.message(lambda message: message.text == 'Слова На Тему Мода 💄')
async def send_dict_school_w(message: types.Message):
    formatted_dict = "\n".join([f"{word} - {translation}" for word, translation in words.job_words.items()])
    await message.reply(formatted_dict, parse_mode=ParseMode.MARKDOWN)