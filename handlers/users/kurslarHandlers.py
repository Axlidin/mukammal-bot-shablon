from aiogram import types

from keyboards.default.starMenu import starMenu_keyboard
from keyboards.inline.courses_inle import kurslar_inle
from loader import dp, bot


@dp.message_handler(text='kurslar')
async def kurslar(message: types.Message):
    await message.answer(
        'Kurslardan birini tanlang',
        reply_markup=kurslar_inle
    )


@dp.callback_query_handler(text='courses')
async def courses(call: types.CallbackQuery):
    await call.answer('Kurslardan birini tanlang', show_alert=True)


@dp.callback_query_handler(text='books')
async def books(call: types.CallbackQuery):
    await call.answer('Kitoblardan birini tanlang', show_alert=True)

@dp.callback_query_handler(text='cancel')
async def calcel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Kurslardan birini tanlang',
        reply_markup=starMenu_keyboard)

