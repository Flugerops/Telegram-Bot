from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Commands")
    ]
], resize_keyboard=True, input_field_placeholder="Choose option")