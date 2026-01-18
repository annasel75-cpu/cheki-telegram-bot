import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID"))

@dp.message_handler(content_types=types.ContentType.ANY)
async def forward_all(message: types.Message):
    user = message.from_user
    header = (
        "📩 Новый чек\n\n"
        f"От: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}\n\n"
    )

    if message.photo:
        await bot.send_message(TARGET_CHAT_ID, header)
        await bot.send_photo(
            TARGET_CHAT_ID,
            message.photo[-1].file_id,
            caption=message.caption or ""
        )
    else:
        await bot.send_message(
            TARGET_CHAT_ID,
            header + (message.text or "Сообщение")
        )

if __name__ == "__main__":
    executor.start_polling(dp)
