from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Команди")
    ],
    [
        KeyboardButton(text="Наша Команда")
    ]
], resize_keyboard=True, input_field_placeholder="Виберіть Опцію")

language_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Англійська🇬🇧")
    ]
], resize_keyboard=True, input_field_placeholder="Виберіть Мову")


user_mode_choice = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Слова По Темам")
    ],

    [
        KeyboardButton(text='Вгадай Переклад Слова')
    ],

    [
        KeyboardButton(text='Поради')
    ],

], resize_keyboard=True, input_field_placeholder="Виберіть Мод")

start_quiz = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Почати квіз")
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
        KeyboardButton(text='Слова На Тему Музика🎵')
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


team_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Посилання на наш проєкт", url="https://github.com/Flugerops/Telegram-Bot")
    ]
])