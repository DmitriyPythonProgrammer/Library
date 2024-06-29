import asyncio

from aiogram import Router
from heandlers.main_heandlers import dp
from utils.create_bot import bot

router = Router()

dp.include_router(router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types()
        )
    except KeyboardInterrupt:
        pass
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
