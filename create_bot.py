import asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from keyboard.inline import bot
from utils.config_reader import config
from handlers.main_handler import router as main_router
from handlers.chat_handler import router as admin

import logging

logging.basicConfig(level=logging.DEBUG)


storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
dp.include_routers(main_router, admin)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())