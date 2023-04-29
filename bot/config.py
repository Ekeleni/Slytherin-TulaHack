from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot('6256618147:AAEY13jG240FJe5jo7_EhDcl22kxAObgiSM')
dp = Dispatcher(bot, storage=storage)

texts = {
    'start': '''Что Где в Туле? — бот для просмотра актуальных мероприятий в Туле
Я смогу:
        - Подобрать интересные для тебя мероприятия
        - Найти ближайшие мероприятия
        - Купить билеты
        - Напомнить о мероприятии''',
    'help': 'https://telegra.ph/CHto-Gde-v-Tule-04-28'}