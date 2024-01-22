from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Команди")
    ],
    [
        KeyboardButton(text="Наша команда")
    ]
], resize_keyboard=True, input_field_placeholder="Виберіть опцію")

language_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/Англійська🇬🇧")
    ]
], resize_keyboard=True, input_field_placeholder="Виберіть мову")

themes_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/Початкові слова")
    ],
    [
        KeyboardButton(text="/Cлова для подорожі")
    ],
    [
        KeyboardButton(text="/Cлова для розмови")
    ]
], resize_keyboard=True, input_field_placeholder="Виберіть тему")

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