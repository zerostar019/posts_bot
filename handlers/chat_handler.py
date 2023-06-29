from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyboard.inline import bot

router = Router()


@router.callback_query(F.data == "approve")
async def forward_story(callback: CallbackQuery):
    text = callback.message.text.split("sep")[1]
    await bot.send_message(
        chat_id="-1001847483219",
        text=text + "\n<em>P.S. История от подписчика</em>"
    )
    await callback.answer()


@router.callback_query(F.data == "reject")
async def delete_msg(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()