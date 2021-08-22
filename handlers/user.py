from aiogram import types, Dispatcher
from keyboard.kb import kb
from config import USERS_VOCALIBARY


async def start_bot(message: types.Message):
    id_user = message.from_user.id
    if id_user not in USERS_VOCALIBARY:
        await message.answer_sticker(sticker='CAACAgQAAxkBAAECtNJhD67C8JamKiIB5FKVq6ZpCE949wAC_xcAAqbxcR5HPSqqjjFcFiAE')
        await message.answer(text='Hello call the command /help, if you want to know more about our bot')
        USERS_VOCALIBARY.update({id_user: []})
    else:
        await message.answer('The bot is running.')


async def help(message: types.Message):
    text_help = 'This is an instruction for using our bot\n' \
                'Here is a list of our commands:\n' \
                '/help - instructions for using the bot\n' \
                '/add_notes - When you call this command, each of your messages will be added to notes ' \
                'until you call the /cancel command\n' \
                '/cancel - this command stops entering notes\n' \
                '/actions - command to view the action with your notes.'
    await message.answer(text_help)


async def greet_kb(message: types.Message):
    await message.answer(text='Choose an Action with Your Notes', reply_markup=kb)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands='start')
    dp.register_message_handler(greet_kb, commands='actions')
    dp.register_message_handler(help, commands='help')
