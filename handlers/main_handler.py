from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboard.inline import start_keyboard
from handlers.story_handler import router as get_story

router = Router(name="Main")
router.include_routers(get_story)


@router.message(F.text == "/start")
async def hello_world(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Доброго времени суток!\n\nПредлагайте Ваши истории из жизни, рассматриваем всех"
             "\nА также здесь Вы можете купить рекламу, либо договориться о взаимном пиаре",
        reply_markup=start_keyboard()
    )


@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
    await hello_world(callback.message, state)
