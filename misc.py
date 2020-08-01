import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import facebook
from twython import Twython
import vk_api
#FACEBOOK
page_access_token = "YOR FACEBOOK ACCESS TOKEN"
graph = facebook.GraphAPI(page_access_token)
#TELEGRAM TOKEN
bot = Bot(token="YOR TELEGRAM BOT TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)
logging.basicConfig(level=logging.INFO)
#TWITTER
APP_KEY = 'YOUR TWITTER APP KEY'
APP_SECRET = 'YOUR TWITTER APP SECRET KEY'
OAUTH_TOKEN = 'YOUR OAUTH TOKEN'
OAUTH_TOKEN_SECRET = 'YOUR OAUTH TOKEN SECRET'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#VKONTAKTE
vk_session = vk_api.VkApi('PHONE', 'PASSWORD')
vk_session.auth()
vk = vk_session.get_api()
