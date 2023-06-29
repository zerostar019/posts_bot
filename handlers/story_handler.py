from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram import Router, F
from keyboard.inline import bot, story_keyboard

router = Router()


class SuggestStory(StatesGroup):
    get_story = State()


@router.callback_query(F.data == "create_story")
async def get_story(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.set_state(SuggestStory.get_story)
    message = await callback.message.answer(
        text="Напишите Вашу историю максимально детально, чтобы читатели смогли полностью погрузиться"
             " в неё!",
        reply_markup=story_keyboard(cancel=True)
    )
    await state.update_data(message_id=message.message_id)
    await callback.answer()


@router.message(SuggestStory.get_story)
async def show_story(message: Message, state: FSMContext):
    data = await state.get_data()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=data.get('message_id')
    )
    username = message.from_user.username
    user_id = message.from_user.id
    await state.clear()
    await bot.send_message(
        chat_id="-939927670",
        text="sep" + message.text + "sep" + "\nUsername: " + f"@{username}" + f"\nID: {user_id}",
        reply_markup=story_keyboard(cancel=None)
    )
    await message.answer(
        text="Спасибо Вам за необычную историю!\n"
             "Вы сможете её увидеть в нашем канале\n"
             "@trash_tallk",
        reply_markup=story_keyboard(main=True)
    )
