import sqlite3

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from crud_functions import *




api = ''

bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

kb = ReplyKeyboardMarkup(resize_keyboard= True)
button_1 = KeyboardButton(text= 'Рассчитать')
button_2 = KeyboardButton(text= 'Информация')
button_3 = KeyboardButton(text= 'Купить!')
button_4 = KeyboardButton(text= 'Регистрация')
kb.add(button_1)
kb.add(button_2)
kb.add(button_3)
kb.add(button_4)

i_kb = InlineKeyboardMarkup()
i_button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data= 'calories')
i_button_2 = InlineKeyboardButton(text='Формула расчета', callback_data= 'formulas')
i_kb.add(i_button_1)
i_kb.add(i_button_2)

i_buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= 'Product1', callback_data= 'product_buying')],
        [InlineKeyboardButton(text= 'Product2', callback_data= 'product_buying')],
        [InlineKeyboardButton(text= 'Product3', callback_data= 'product_buying')],
        [InlineKeyboardButton(text= 'Product4', callback_data= 'product_buying')],
    ]
)



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


@dp.callback_query_handler(text= 'product_buying')
async def set_age(call):
   await call.message.answer('Вы успешно приобрели продукт', reply_markup= kb)
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

@dp.message_handler(text = ['Купить!'])
async def get_buying_list(message):
    prod = get_all_products()
    for i in range(4):
        await message.answer(f'Название: {prod[0 + i][1]} | Описание: {prod[0 + i][2]} | Цена: {prod[0 + i][3]}')
        with open(f'photos/{i + 1}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки', reply_markup= i_buy_kb)


@dp.message_handler(text = ['Регистрация'])
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит)')
    await RegistrationState.username.set()


@dp.message_handler(state= RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email')
        await RegistrationState.email.set()

@dp.message_handler(state= RegistrationState.email)
async def set_email(message, state):
        await state.update_data(email=message.text)
        await message.answer('Введите свой возраст')
        await RegistrationState.age.set()

@dp.message_handler(state= RegistrationState.age)
async def set_age(message, state):
        await state.update_data(age=message.text)
        data = await state.get_data()
        add_user(data['username'], data['email'], data['age'])
        await message.answer('Вы успешно зарегистрированы!')
        await state.finish()


@dp.message_handler()
async def all_messeges(messege):
    await messege.answer('Введите команду /start для начала общения!')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)