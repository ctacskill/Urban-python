from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, default_state
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''

bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



kb = ReplyKeyboardMarkup(resize_keyboard= True)
button_1 = KeyboardButton(text= 'Рассчитать')
button_2 = KeyboardButton(text= 'Информация')
kb.add(button_1)
kb.add(button_2)


i_kb = InlineKeyboardMarkup()
i_button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data= 'calories')
i_button_2 = InlineKeyboardButton(text='Формула расчета', callback_data= 'formulas')
i_kb.add(i_button_1)
i_kb.add(i_button_2)



@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = i_kb)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer(' (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x 1.55')
    await call.answer()

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup = kb)


@dp.callback_query_handler(text= 'calories')
async def set_age(call):
   await call.message.answer('Введите свой возраст')
   await UserState.age.set()
   await call.answer()


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