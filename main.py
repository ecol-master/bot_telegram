from aiogram import Bot, Dispatcher, executor, types
import logging
from handlers.user import register_handlers
from handlers.callback_handler import register_callback_query
import config
from handlers.notes import register_notes_handlers
from fsm.states_add_notes import register_fsm_bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=config.TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)
logging.basicConfig(level=logging.INFO)

register_handlers(dp)
register_callback_query(dp)
register_notes_handlers(dp)
register_fsm_bot(dp)

if __nameпше__ == '__main__':
    executor.start_polling(dp)