from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM(StatesGroup):
    city = State()


async def start_to_get_city(msg: types.Message):
    await FSM.city.set()
    await msg.answer('City?')


async def cancel(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        return
    await state.finish()
    await msg.reply('Canceled')


async def get_city(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = msg.text
    await msg.answer(str(data['city']))
    await state.finish()




def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_to_get_city, commands=['weather'], state=None)
    dp.register_message_handler(cancel, state='*', commands="back")
    dp.register_message_handler(cancel, Text(equals='back', ignore_case=True), state='*')
    dp.register_message_handler(get_city, state=FSM.city)