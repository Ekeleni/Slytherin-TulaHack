from aiogram import executor
from config import dp
from chat import init_chat
from creator import init_creator


async def on_startup(_):
    print('Start')

init_creator(dp)
init_chat(dp)
executor.start_polling(dp, skip_updates=True)
