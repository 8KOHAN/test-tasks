from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

async def main():
    
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token)
    dp = Dispatcher()

    print("bot start")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
