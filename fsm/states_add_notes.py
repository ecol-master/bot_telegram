from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from config import USERS_VOCALIBARY
from aiogram.dispatcher import FSMContext


class Form(StatesGroup):
    notes = State()


async def add_notes(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    if id_user in USERS_VOCALIBARY:
        await Form.notes.set()
        await message.answer('OK, Send me note wich you want to add')
    else:
        await message.answer(
            'You have not started the bot for this, call the command - /start')
        await state.finish()


async def answer_to_addnotes(message: types.Message, state: FSMContext):
    note_add = message.text
    id_user = message.from_user.id
    # if not message.get_command('cancel'):
    # USERS_VOCALIBARY[id_user].append(f'✏{note_add}✏')
    # await message.answer('Note added successfully опа тут работает ☑')
    # else:
    await message.answer('Сompleted ☑')
    await state.finish()


async def finish_state(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    await message.answer('Completed ☑')
    await message.state()


def register_fsm_bot(dp: Dispatcher):
    dp.register_message_handler(add_notes, state=None, commands='add_notes')
    dp.register_message_handler(answer_to_addnotes, state=Form.notes)
    dp.register_message_handler(finish_state, commands='cancel', state='*')
