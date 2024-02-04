from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

exit_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад", callback_data="exit")
    ]
])

inline_themes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Початкові Слова 💪", callback_data= "start_words")
    ],
    [
        InlineKeyboardButton(text="Cлова На Тему Подорож ✈️", callback_data= "trip_words")
    ],
    [
        InlineKeyboardButton(text="Слова На Тему Їжа 🍌", callback_data= "food_words")
    ],
    
])