from aiogram import Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import database as db
from config import bot, dp, is_valid_date


class Event(StatesGroup):
    name = State()
    text = State()
    date = State()
    time = State()
    price = State()
    address = State()


async def create_event_start(message: Message):
    await bot.send_message(message.chat.id, 'Отлично, давай! Введи название мероприятия')
    await Event.name.set()


async def reg_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await bot.send_message(message.chat.id, 'Отлично! А теперь описание')
    await Event.next()


async def reg_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await bot.send_message(message.chat.id, 'Прикольно. А теперь дату твоего события в формате: ХХ.ХХ.ХХ')
    await Event.next()


async def reg_date(message: Message, state: FSMContext):
    async with state.proxy() as data:
        if is_valid_date(message.text):
            data['date'] = message.text
            await bot.send_message(message.chat.id, 'А теперь во сколько все это будет?')
            await Event.next()
        else:
            await bot.send_message(message.chat.id, 'Эй! Твое событие так и не произойдет... давай другую дату =)')


async def reg_time(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await bot.send_message(message.chat.id, 'А стоит сколько? Если бесплатно - пиши 0, не стесняйся')
        await Event.next()


async def reg_price(message: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = int(message.text)
            check = int(data['price'])
            await bot.send_message(message.chat.id, 'Найс. И последнее... Где оно?')
            await Event.next()
        except Exception as ex:
            print(ex)
            await bot.send_message(message.chat.id, 'Эй! Я же просил!. Нука число напиши')


async def reg(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        db.add_event_load(message.chat.id, data['name'], data['text'], data['date'], data['time'], data['price'], data['address'])
        await bot.send_message(message.chat.id, 'Ну вот и все. Теперь ждем, пока модератор примет заявку. Спасибо')
        await state.finish()


async def my_events(message: Message):
    id = 0
    result = db.get_my_events(message.chat.id)
    if not result:
        await bot.send_message(message.chat.id, 'Их еще нет (')
    else:
        if len(result) == 1:
            await bot.send_message(message.chat.id, f'{result[id][2]}\n{result[id][3]}\n\nДата: {result[id][4]}\nВремя: {result[id][5]}\nСтоимость: {result[id][6]}')
        else:
            for i in range(len(result)):
                await bot.send_message(message.chat.id,
                                       f'{result[i][2]}\n{result[i][3]}\n\nДата: {result[i][4]}\nВремя: {result[i][5]}\nСтоимость: {result[i][6]}')


def init_creator(dp: Dispatcher):
    dp.register_message_handler(create_event_start, lambda message: message.text == 'Создать')
    dp.register_message_handler(reg_name, state=Event.name)
    dp.register_message_handler(reg_text, state=Event.text)
    dp.register_message_handler(reg_date, state=Event.date)
    dp.register_message_handler(reg_time, state=Event.time)
    dp.register_message_handler(reg_price, state=Event.price)
    dp.register_message_handler(reg, state=Event.address)
    dp.register_message_handler(my_events, lambda message: message.text == 'Мои')


