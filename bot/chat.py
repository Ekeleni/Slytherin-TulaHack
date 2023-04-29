from aiogram.types import Message
from aiogram import Dispatcher
from config import texts, bot, dp
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


async def start_message(message: Message):
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(KeyboardButton('Помощь'), KeyboardButton('Мероприятия'))
    await bot.send_message(message.chat.id, texts['start'], parse_mode='HTML', reply_markup=key)


async def help_message(message: Message):
    await bot.send_message(message.chat.id, f'Лечу на помощь: \n{texts["help"]}')


async def change_day(message: Message):
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(KeyboardButton('Сегодня'), KeyboardButton('Завтра'), KeyboardButton('На этой неделе'),
            KeyboardButton('В это месяце'))
    await bot.send_message(message.chat.id, 'Выбери дату мероприятия:', reply_markup=key)


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, lambda message: message.text == "Помощь")
    dp.register_message_handler(change_day, lambda message: message.text == "Мероприятия")
