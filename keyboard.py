from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Commands")
    ]
], resize_keyboard=True, input_field_placeholder="Choose option")

coom_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="/talk")
    ],
    [
        KeyboardButton(text="/casino")
    ],
    [
        KeyboardButton(text="/dice")
    ]
],  resize_keyboard=True, input_field_placeholder="Your commands", one_time_keyboard=True)