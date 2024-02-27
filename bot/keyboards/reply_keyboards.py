from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

language_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Англійська🇬🇧")
    ],
    [
        KeyboardButton(text="Французька🇫🇷")
    ],
    [
        KeyboardButton(text="Німецька🇩🇪")
    ],
    [
        KeyboardButton(text="Іспанська🇪🇸")
    ],
    [
        KeyboardButton(text="Італійська🇮🇹")
    ]
], resize_keyboard= True, input_field_placeholder="Оберіть мову", one_time_keyboard=True)


user_mode_choice = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Слова По Темам")
    ],

    [
        KeyboardButton(text='Вгадай Переклад Слова')
    ],

    [
        KeyboardButton(text='Асистент')
    ],

    [
        KeyboardButton(text='Перекладач')
    ],
    
    [
        KeyboardButton(text='Вибір Мови')
    ],
    
    [
        KeyboardButton(text='Контакти Розробників')
    ],

], resize_keyboard=True, input_field_placeholder="Виберіть Режим", one_time_keyboard=True)

quiz_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Продовжити")
    ],
    [
        KeyboardButton(text="Я не можу відповісти")
    ],
    [
        KeyboardButton(text="Вийти")
    ]

], resize_keyboard=True, input_field_placeholder="Натисніть коли готові")


themes_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Початкові Слова 💪")
    ],
    
    [
        KeyboardButton(text="Cлова На Тему Подорож ✈️")
    ],
    
    [
        KeyboardButton(text="Слова На Тему Їжа 🍌")
    ],
    
    [
        KeyboardButton(text="Слова На Тему Кольори 🟣")
    ],
    
    [
        KeyboardButton(text='Cлова На Тему Розмова 🗣')
    ],

    [
        KeyboardButton(text= "Слова На Тему Тварини 🐍")
    ],
    
    [
        KeyboardButton(text="Слова На Тему Айті 💻")
    ],
    
    [
        KeyboardButton(text="Слова На Тему Школа 🏫")
    ],

    [
        KeyboardButton(text='Слова На Тему Спорт ⚽️')
    ],

    [
        KeyboardButton(text='Слова На Тему Музика 🎵')
    ],

    [
        KeyboardButton(text='Слова На Тему Квартира 🏘')
    ],

    [
        KeyboardButton(text='Слова На Тему Робота 💼')
    ],

    [
        KeyboardButton(text='Слова На Тему Фільми 🎬')
    ],

    [
        KeyboardButton(text='Слова На Тему Мода 💄')
    ],

    [
        KeyboardButton(text='Слова На Тему Питання ❓')
    ]

], resize_keyboard=True, input_field_placeholder="Виберіть Тему", one_time_keyboard=True)


comm_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/language")
    ],
    [
        KeyboardButton(text="")
    ],
    [
        KeyboardButton(text="")
    ]
],  resize_keyboard=True, input_field_placeholder="Ваші команди", one_time_keyboard=True)

translator_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="❌")
    ],
    
    [
        KeyboardButton(text="🔄️")
    ]
],resize_keyboard=True)



exit_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Повернутися в меню")
    ]
],resize_keyboard=True, one_time_keyboard=True)

quiz_start = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Продовжити")
    ],
    [
        KeyboardButton(text="Вийти")
    ]





], resize_keyboard=True, one_time_keyboard=True)