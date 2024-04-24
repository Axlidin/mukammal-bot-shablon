import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.starMenu import starMenu_keyboard
from keyboards.inline.courses_inle import Cancel
from loader import dp, bot
from states.PersonData_states import Person_datas

@dp.message_handler(commands='html_info')
async def html_info(message: types.Message):
    await message.answer(f"<b>bu matn qalin</b>\n"
                         f"<i>bu esa qiya matn</i>\n"
                         f"<u>bu underline</u>\n"
                         f"<s>bu o'chirilgan matn</s>\n"
                         f"<a href='https://google.com'>buyerga bosing</a>\n"
                         f"<code>bu esa kod</code>")#tag

@dp.message_handler(commands='markdown_info')
async def mk_info(message: types.Message):
    await message.answer(f"*bu matn qalin\.*\n"
                         # f"<i>bu esa qiya matn</i>\n"
                         # f"<u>bu underline</u>\n"
                         # f"<s>bu o'chirilgan matn</s>\n"
                         # f"<a href='https://google.com'>buyerga bosing</a>\n"
                         f"`bu esa kod`", parse_mode=types.ParseMode.MARKDOWN_V2)#tag