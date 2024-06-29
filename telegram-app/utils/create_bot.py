from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from config import REDIS_URL, TOKEN
import logging

logging.basicConfig(level=logging.INFO)
storage = RedisStorage.from_url(REDIS_URL)
dp = Dispatcher(storage=storage)
bot = Bot(TOKEN)
