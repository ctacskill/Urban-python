from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, default_state
from aiogram.dispatcher.filters.state import StatesGroup
from pyexpat.errors import messages

api = ''

bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()





@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!')


@dp.message_handler(text = ['Colories'])
async def set_age(message):
   await message.answer('Введите свой возраст')
   await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_colories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    colories_1 = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    colories = round(colories_1 * 1.55, 0)
    await message.answer(colories)
    await state.finish()



@dp.message_handler()
async def all_messeges(messege):
    await messege.answer('Введите команду /start для начала общения!')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)