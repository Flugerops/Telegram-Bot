from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Commands")
    ],
    [
        KeyboardButton(text="Our team")
    ]
], resize_keyboard=True, input_field_placeholder="Choose option")

comm_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/talk")
    ],
    [
        KeyboardButton(text="/casino")
    ],
    [
        KeyboardButton(text="/die")
    ]
],  resize_keyboard=True, input_field_placeholder="Your commands", one_time_keyboard=True)

team_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Our project link", url="https://github.com/Flugerops/Telegram-Bot")
    ]
])