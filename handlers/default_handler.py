from aiogram import types
from misc import dp, graph, twitter


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    await message.answer("I don't know what to do with this ... But you can send me a /post command and I will publish a post on social networks")