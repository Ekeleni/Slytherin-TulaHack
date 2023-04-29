from aiogram import Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from config import bot, dp


async def create_event_start(message: Message):
    await bot.send_message(message.chat.id, 'Тут!')


def init_creator(dp: Dispatcher):
    dp.register_message_handler(create_event_start, lambda message: message.text == 'Создать')
