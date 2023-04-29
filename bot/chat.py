from aiogram.types import Message
from aiogram import Dispatcher
from config import texts, bot, dp


async def start_message(message: Message):
    await bot.send_message(message.chat.id, texts['start'], parse_mode='HTML')


async def help_message(message: Message):
    await bot.send_message(message.chat.id, f'Лечу на помощь: \n{texts["help"]}')


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])