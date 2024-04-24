# import re
#
# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from data.config import ADMINS
# from keyboards.default.starMenu import starMenu_keyboard
# from keyboards.inline.courses_inle import Cancel
# from loader import dp, bot
# from states.PersonData_states import Person_datas
#
# email_check = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
#
# info_datas = {}
# print(info_datas)
# @dp.message_handler(commands='start')
# async def anketaStart(msg: types.Message):
#     await msg.answer('Ismingizni kiriting...')
#     await Person_datas.next()
#
# @dp.message_handler(state=Person_datas.firstname)
# async def anketaFirstname(msg: types.Message, state: FSMContext):
#     await state.update_data(
#         {'name': msg.text}
#     )
#     await msg.answer('Yoshingizni kiriting...')
#     await Person_datas.next()
#
#
# @dp.message_handler(state=Person_datas.age)
# async def anketaAge(msg: types.Message, state: FSMContext):
#     if msg.text.isdigit():
#         await state.update_data(
#             {'age': msg.text}
#         )
#         await msg.answer('Email manzilingizni kiriting...')
#         await Person_datas.next()
#     else:
#         await msg.answer('Yosh kiritishda xatolik yuz berdi, iltimos qaytadan kiriting...')
#
#
# @dp.message_handler(state=Person_datas.email)
# async def anketaEmail(msg: types.Message, state: FSMContext):
#     if re.match(email_check, msg.text):
#         await state.update_data(
#             {'email': msg.text}
#         )
#         await msg.answer('Telefon manzilingizni kiriting...')
#         await Person_datas.next()
#     else:
#         await msg.answer('Email manzilini kiritishda xatolik yuz berdi, iltimos qaytadan kiriting...')
#
#
# @dp.message_handler(state=Person_datas.phone)
# async def anketaPhone(msg: types.Message, state: FSMContext):
#     global info_datas
#     if msg.text.isdigit() and len(msg.text) == 9:
#         await state.update_data(
#             {'phone': f"+998{msg.text}"}
#         )
#
#         datas = await state.get_data()
#         ism = datas.get('name')
#         yosh = datas.get('age')
#         email = datas.get('email')
#         tel = datas.get('phone')
#         info_datas = {
#             'name': ism,
#             'age': yosh,
#             'email': email,
#             'phone': tel}
#         await msg.answer(f"Siz anketani muvofaqqiyatli to'ldirdingiz>>>\n"
#                          f"ism: {ism}\n"
#                          f"yosh: {yosh}\n"
#                          f"email: {email}\n"
#                          f"tel: {tel}", reply_markup=starMenu_keyboard)
#         await bot.send_message(chat_id=ADMINS[0],
#                                text=f"Siz anketani muvofaqqiyatli to'ldirdingiz>>>\n"
#                                     f"ism: {ism}\n"
#                                     f"yosh: {yosh}\n"
#                                     f"email: {email}\n"
#                                     f"tel: {tel}")
#         await state.finish()
#         print(info_datas)
#     else:
#         await msg.answer('Telefon nomerini kiritishda xatolik yuz berdi, iltimos qaytadan kiriting...')
#
# @dp.message_handler(text='about me')
# async def anketaAbout(msg: types.Message):
#     global info_datas
#     text = ""
#     for k, v in info_datas.items():
#         text += f"{k}:{v}\n"
#     await msg.answer(text, reply_markup=Cancel)