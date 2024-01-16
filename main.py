from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
# from dif_unc import command_list
import random
load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")

inline_keyboard = InlineKeyboardMarkup(row_width=3)


button1 = InlineKeyboardButton("Button 1", callback_data="button1")
button2 = InlineKeyboardButton("Button 2", callback_data="button2")
button3 = InlineKeyboardButton("Button 3", callback_data="button3")
button4 = InlineKeyboardButton("Button 4", callback_data="button4")
button5 = InlineKeyboardButton("Button 5", callback_data="button5")
button6 = InlineKeyboardButton("Button 6", callback_data="button6")

inline_keyboard.add(button1, button2, button3)
inline_keyboard.add(button4, button5, button6)



dp = Dispatcher()



@dp.message(Command(button1))
async def send_message(message: Message) -> None:
    await message.answer("Hello I`m a stupid bot")

@dp.message(Command(button2))
async def send_dice(message: Message) -> None:
    await message.answer_dice("🎲")

@dp.message(Command(button3))
async def send_casion(message: Message) -> None:
    await message.answer_dice("🎰")


@dp.message(Command(button4))
async def send_casion(message: Message) -> None:
    await message.answer("I Have 3 developers")
    await message.answer_contact(phone_number='+380 66 383 11 17', first_name='Nazar')
    await message.answer_contact(phone_number='+380 97 693 81 92', first_name='Bogdan')
    await message.answer_contact(phone_number='+380 98 019 58 11', first_name='Leonid')


# @dp.message(Command('allcommands'))
# async def send_all_comands(message: Message) -> None:
    # await message.reply(command_list)



@dp.message(Command(button5))
async def send_all_comands(message: types.Message) -> None:
    await message.reply(text="It's Team - GitHub\nhttps://github.com/Flugerops/Telegram-Bot")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())