from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot
from utils.config_reader import config

bot = Bot(token=str(config.API_TOKEN.get_secret_value()), parse_mode="HTML")


def start_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Предложить историю", callback_data="create_story")],
        [InlineKeyboardButton(text="Купить рекламу", url="https://t.me/ropien10"),
         InlineKeyboardButton(text="Взаимопиар", url="https://t.me/ropien10")]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def story_keyboard(cancel=None, main=None) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if cancel is not None:
        builder.button(text="Отмена", callback_data="cancel")
        return builder.as_markup()
    if main is not None:
        builder.button(text="Главное меню", callback_data="cancel")
        return builder.as_markup()
    builder.button(text="Одобрить", callback_data="approve")
    builder.button(text="Треш, отклонить", callback_data="reject")
    return builder.as_markup()

