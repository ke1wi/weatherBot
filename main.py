from aiogram import types
from aiogram.utils import executor
from create_bot import dp


import FSM


async def on_start(_):
    print("Bot is working...")


FSM.register_handlers(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)