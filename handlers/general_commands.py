from aiogram import types
from misc import dp, graph, twitter

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Howdy ho! So far I can only do one thing: on the /post command, send your posts to social networks")