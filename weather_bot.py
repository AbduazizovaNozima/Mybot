from aiogram import types, Bot, Dispatcher, F
import logging, sys, asyncio
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import re
from integration import get_UZS

TOKEN = '7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM'
bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(text=f"Assalomu alaykum {full_name} dollar kurs ma'lumotlariga xush kelibsiz \n Dollar raqamini kiriting so'mda qancha bo'lishini sizga chiqazib beraman")


@dp.message()
async def send_rate_info(message: types.Message):
    user_input = message.text.strip() 

    if user_input.replace('.', '', 1).isdigit(): 
        usd_amount = float(user_input)  
        valyuta_data = get_UZS(usd_amount) 
        await message.answer(valyuta_data)
    else:
        await message.answer("Iltimos, faqat raqamli dollar miqdorini kiriting.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

# @dp.message(CommandStart())
# async def start(message: types.Message):
#     full_name = message.from_user.full_name
#     await message.answer(text=f"Assalomu alaykum {full_name} ob-havo bot ma'lumotlariga xush kelibsiz")

# @dp.message()
# async def send_weather_info(message: types.Message):
#     weather_data = get_weather_data(message.text)
#     await message.answer(weather_data)


# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())



