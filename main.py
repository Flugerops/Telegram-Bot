from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command
from aiogram.methods import send_message

import keyboard


load_dotenv()
print(getenv("TOKEN"))
TOKEN = getenv("TOKEN")


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=keyboard.kb)


@dp.message(Command("talk"))
async def send_message(message: Message) -> None:
    await message.answer("Hello i`m stupid bot")

@dp.message(Command("dice"))
async def send_dice(message: Message) -> None:
    await message.answer_dice("🎲")

@dp.message(Command("casino"))
async def send_casion(message: Message) -> None:
    await message.answer_dice("🎰")

@dp.message()
async def echo(message: Message):
    temp_msg = message.text.lower()
    if temp_msg == "commands":
        await message.answer("Your commands: ", reply_markup=keyboard.comm_kb)
    if temp_msg == "our team":
        await message.answer("Zmiini_Novatori", reply_markup=keyboard.team_kb)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())