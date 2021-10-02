from aiogram import Dispatcher, types
from config import USERS_VOCALIBARY


async def check_callback(callback: types.CallbackQuery):
    bot = callback.bot
    id_user = callback.from_user.id
    await bot.answer_callback_query(callback.id)
    if id_user in USERS_VOCALIBARY:
        if callback.data == 'see_my_notes':
            notes_user = USERS_VOCALIBARY[id_user]
            if notes_user != []:
                await bot.send_message(chat_id=callback.message.chat.id, text='📝Your Notes\n' + '\n'.join(notes_user))
            else:
                await bot.send_message(chat_id=callback.message.chat.id, text='Your notes are blank.')
        elif callback.data == 'delet_kb':
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        else:
            USERS_VOCALIBARY[id_user].clear()
            await bot.send_message(chat_id=callback.message.chat.id,
                                   text='Your notes have been successfully deleted.☑', )
    else:
        await bot.send_message(chat_id=callback.message.chat.id, text='First, call the command /start')


def register_callback_query(dp: Dispatcher):
    dp.register_callback_query_handler(check_callback, text=['see_my_notes', 'delet_notes', 'delet_kb'])
