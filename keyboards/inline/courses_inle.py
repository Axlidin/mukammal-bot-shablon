from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kurslar_inle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data='courses'),
            InlineKeyboardButton(text="Kitoblar", callback_data='books'),
        ],
        [
            InlineKeyboardButton(text="🔙 ortga", callback_data='cancel'),
        ]
    ]
)
Cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 ortga", callback_data='cancel'),
        ]
    ]
)