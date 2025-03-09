import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
import asyncio

API_TOKEN = '1895077818:AAHRVL99uz_uEc_cJ4tvXti1V3nB-d_ZF4I'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хэндлер для команды /start
@dp.message(Command("start"))
async def on_start(message: types.Message):
    await message.answer("<b>Hello, I'm your baby!</b>", parse_mode=ParseMode.HTML)

# Устанавливаем webhook
async def set_webhook():
    webhook_url = 'https://zbestdeep.onrender.com'  # Укажи URL, куда будут приходить обновления
    await bot.set_webhook(webhook_url)

async def main():
    # Выбор между webhook и polling:
    use_webhook = False  # Установите True для использования webhook

    if use_webhook:
        await set_webhook()  # Устанавливаем webhook
    else:
        # Если polling
        await bot.delete_webhook()  # Удаляем webhook, если он был установлен
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  # Запуск асинхронной задачи
