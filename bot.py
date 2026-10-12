import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8710116991:AAEP5qQ59iUkB0HJckJj5FlufAkbHNgx4PA"
GROUP_ID = -1002720925459

bot = Bot(TOKEN)
dp = Dispatcher()
waiting = set()


@dp.message(CommandStart(), F.chat.type == "private")
async def start(message: Message):
    waiting.add(message.from_user.id)
    await message.answer("ну давай, оправдай свои 42 хромосомы")


@dp.message(F.chat.type == "private")
async def forward(message: Message):
    if message.from_user.id in waiting:
        await bot.copy_message(
            chat_id=GROUP_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
        waiting.discard(message.from_user.id)
        await message.answer("ладна")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
