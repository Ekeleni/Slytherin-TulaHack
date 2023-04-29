from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime

storage = MemoryStorage()
bot = Bot('6256618147:AAEY13jG240FJe5jo7_EhDcl22kxAObgiSM')
dp = Dispatcher(bot, storage=storage)

texts = {
    'start': '''
     Привет, друг! Я помогу тебе найти интересное и классное мероприятие в Туле. 
     Просто выбери интересное тебе мероприятие или пришли свою геопозицию
    ''',
    'help': 'https://telegra.ph/CHto-Gde-v-Tule-04-28'
}


def get_event_date(date):

    date_current = datetime.now()
    match date:
        case 'Сегодня':
            return [[f'{date_current.day}.0{date_current.month}.{date_current.year}']]
        case 'Завтра':
            return [[f'{int(date_current.day) + 1}.0{date_current.month}.{date_current.year}d']]
        case 'На этой неделе':
            date_time = list()
            for i in range(7 - date_current.weekday()):
                date_time.append([f'{int(date_current.day) + i}.0{date_current.month}.{date_current.year}'])
            return date_time

