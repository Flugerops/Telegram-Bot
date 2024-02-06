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
    [
        InlineKeyboardButton(text="Слова На Тему Кольори 🟣", callback_data= "colors_words")
    ],
    
    [
        InlineKeyboardButton(text='Cлова На Тему Розмова 🗣', callback_data= "conversation_words")
    ],

    [
        InlineKeyboardButton(text= "Слова На Тему Тварини 🐍", callback_data= "animals_theme_words")
    ],
    
    [
        InlineKeyboardButton(text="Слова На Тему Айті 💻", callback_data= "it_words")
    ],
    
    [
        InlineKeyboardButton(text="Слова На Тему Школа 🏫", callback_data= "school_words")
    ],
    
    [
        InlineKeyboardButton(text='Слова На Тему Спорт ⚽️', callback_data= "sprt_words")
    ],

    [
        InlineKeyboardButton(text='Слова На Тему Музика 🎵', callback_data= "music_words")
    ],

    [
        InlineKeyboardButton(text= 'Cлова На Тему Квартира 🏘', callback_data= "house_words")
    ],

    [
        InlineKeyboardButton(text='Слова На Тему Робота 💼', callback_data= "job_words")
    ],

    [
        InlineKeyboardButton(text='Слова На Тему Фільми 🎬', callback_data= "film_words")
    ],

    [
        InlineKeyboardButton(text='Слова На Тему Мода 💄', callback_data= "fasion_words")
    ]
    
])