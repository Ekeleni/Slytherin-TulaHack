from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

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
