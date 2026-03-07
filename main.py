import os, asyncio, logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handles.root import root
from handles.user import user
from database.db import create_tables

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN", "NAN")
if TOKEN == "NAN":
    raise ValueError("Токен отсутствует в .env")

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(root, user)
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
