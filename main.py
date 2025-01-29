from aiogram import types, Bot, Dispatcher, F
import logging, sys, asyncio
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import re

TOKEN = '7864725145:AAGoT3BWPa7cdiQPxuzirG-sOK4MqihijZg'
bot = Bot(token=TOKEN)

PHONE_REGEX = r"\+998[0-9]{9}"
EMAIL_REGEX = r"[a-z]+@[a-z]+\.[a-z]{0,3}"

def is_phone(text):
    return bool(re.match(PHONE_REGEX, text))
def is_email(text):
    return bool(re.match(EMAIL_REGEX, text))

class Register(StatesGroup):
    ism = State()
    yosh = State()
    tel_raqam = State()
    email = State()

def buttons():
    kb = [
        [types.InlineKeyboardButton(text='Ha', callback_data='ha'),
        types.InlineKeyboardButton(text='yoq', callback_data='yoq')
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Salom! Botimizga xush kelibsiz, Ro'yhatdan o'tish uchun /register tugmasini bosing")
    # print(message.chat.id)
@dp.message(F.text == '/register')
async def cmd_start(message: types.Message, state:FSMContext):
    await message.answer("Ismingizni kiriting: ")
    await state.set_state(Register.ism)

@dp.message(Register.ism)
async def set_ism(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await message.answer(text='Yoshingizni kiriting: ')
    await state.set_state(Register.yosh)

@dp.message(Register.yosh)
async def set_ism(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer(text="yosh faqat raqamlardan iborat bo'ladi")
    await state.update_data(yosh=message.text)
    await message.answer(text='Tel_raqam kiriting: ')
    await state.set_state(Register.tel_raqam)

@dp.message(Register.tel_raqam)
async def set_ism(message: types.Message, state: FSMContext):
    if not is_phone(message.text):
        return await message.answer(text="Tel raqam notogri kiritildi")
    await state.update_data(tel_raqam=message.text)
    await message.answer(text='Email kiriting: ')
    await state.set_state(Register.email)

@dp.message(Register.email)
async def set_ism(message: types.Message, state: FSMContext):
    if not is_email(message.text):
        return await message.answer(text="Email notogri kiritildi")
    await state.update_data(email=message.text)
    data = await state.get_data()
    register_info = f'Malumotlar togrimi? \nIsmi {data['ism']}, \nYoshi {data['yosh']}, \nTel_raqam {data['tel_raqam']}, \nEmail {data['email']}'
    await message.answer(text=register_info, reply_markup=buttons())


@dp.callback_query(Register.email)
async def send_msg(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'ha':
        data = await state.get_data()
        register_info = f'Ismi {data['ism']}, \nYoshi {data['yosh']}, \nTel_raqam {data['tel_raqam']}, \nEmail {data['email']}'
        await bot.send_message(chat_id=6387861882, text=register_info)
        await callback.message.answer(text='Royhatdan otdingiz')
    elif callback.data == 'yoq':
        await callback.message.answer(text='Sorov bekor qilindi')
    await state.clear()
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


