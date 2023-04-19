from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import os


bot = (Bot(token=os.getenv('TOKEN')))
dp = Dispatcher(bot)


async def on_start(_):
    print("Bot is working...")

@dp.message_handler(commands=['weather'])
async def startCommand(msg: types.Message):
    await msg.answer('Im working...')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)