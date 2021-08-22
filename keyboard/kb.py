from aiogram import types

kb = types.InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
button1 = types.InlineKeyboardButton(
    text='See My Notes', callback_data='see_my_notes'
)

button2 = types.InlineKeyboardButton(
    text='Delete Notes', callback_data='delet_notes'
)

button3 = types.InlineKeyboardButton(
    text='Exit', callback_data='delet_kb'
)
kb.insert(button1)
kb.insert(button2)
kb.insert(button3)
