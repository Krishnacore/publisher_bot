from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp, graph, twitter, vk

class CreatePost(StatesGroup):
    waiting_for_post_body = State()
    waiting_for_post_link = State()

@dp.message_handler(commands=['post'], state="*")
async def post_step_1(message: types.Message):
    await message.answer('Enter post text (without link):')
    await CreatePost.waiting_for_post_body.set()

@dp.message_handler(state = CreatePost.waiting_for_post_body, content_types = types.ContentTypes.TEXT)
async def post_step_2(message: types.Message, state: FSMContext):
    await state.update_data(post_body = message.text)
    await CreatePost.next()
    await message.answer('Enter link:')
    await CreatePost.waiting_for_post_link.set()

@dp.message_handler(state = CreatePost.waiting_for_post_link, content_types = types.ContentTypes.TEXT)
async def post_step_3(message: types.Message, state: FSMContext):
    await state.update_data(post_link = message.text)
    user_data = await state.get_data()
    await message.answer(f"Post text: {user_data['post_body']}\n"
                         f"LInk: {user_data['post_link']}\n")
    msg = str(user_data['post_body'])
    link = str(user_data['post_link'])
    msg_link = msg + '\n' + link
    twitter.update_status(status = msg_link)
    graph.put_object(parent_object = '107858594357153', connection_name = 'feed', message = msg, link = link)
    print(vk.wall.post(owner_id = '-167746555', from_group = 1 ,message = msg, attachments = link))
    print('OK')
    await state.finish()
