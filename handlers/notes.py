from config import USERS_VOCALIBARY
from aiogram import types, Dispatcher


async def delet_all_notes(message: types.Message):
    for key in USERS_VOCALIBARY:
        USERS_VOCALIBARY[key].clear()
    await message.answer('Hi Boss. All users notes were successfully deleted.☑')


async def spam(messsage: types.Message):
    messsage.bot.send_file()
    for i in range(100):
        await messsage.answer('Игорь хохлябма, го на звонок!')


def register_notes_handlers(dp: Dispatcher):
    # dp.register_message_handler(add_notes, commands='add_notes')
    dp.register_message_handler(delet_all_notes, commands='delet_allnotes_all_users')
    dp.register_message_handler(spam, commands='call')
