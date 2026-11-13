# =========================IMPORT========================= #
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

#routers
from Datee import router as date_router
from Gift import router as gift_router
from Info import router as info_router
from Remove import router as remove_router
from myid import router as telegram_info_router


#tasks
from tasks import clear_daily_list, daily_date
from today import congratulated_today
from congratulations import congratulations
from datebase import datebase


#keyboard&TOKEN
from myid import keyboard
from strTOK import BOT_TOKEN

# =========================SETTINGS========================= #
TELEGRAM_TOKEN = BOT_TOKEN
ADMIN = '1054191711'

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
Private_Keyboard = keyboard


dp.include_router(remove_router)
dp.include_router(date_router)
dp.include_router(info_router)
dp.include_router(gift_router)
dp.include_router(telegram_info_router)

# =========================DataBase========================= #
database = datebase
congrat = congratulations
today_congratulated = congratulated_today

# =========================Keyboard========================= #

# =========================FUNCTIONS========================= #
@dp.message(CommandStart())
async def strart_instruction(message: Message):
    await message.answer(
        text="<b>Hi! I'm DailyBot.</b>\n"
        
             "<b>Here are my commands:</b>\n\n"
             
             "<code>/date</code> - <b>add your name and birthdate to database</b>\n"
             "<blockquote><b>Example: <i>/date Name Surname DD-MM-YYYY</i></b></blockquote>\n"
             "<blockquote><b>Also: <i>/date Name - DD-MM-YYYY</i></b></blockquote>\n\n"
             
             "<code>/gift</code> - <b>add your congratulation in the database</b>\n"
             "<blockquote><b>Example: <i>/gift your_text</i></b></blockquote>\n"
             "If you need to enter name in text , write like this:<code>{name}</code>\n"
             "<blockquote><b>Example: <i>/gift Поздравляю тебя {name}!</i></b></blockquote>\n\n"

             "<code>/remove</code> - <b>delete member from the database</b>\n"
             "<blockquote><b>Example: <i>/remove name DD-MM-YYYY</i></b></blockquote>\n"
             "<blockquote><i><b>/remove Ivan 11-09-2001</b></i></blockquote>\n\n"
             
             "<code>/info</code> - <b>send database in this chat</b>",
        parse_mode="HTML"
    )

# =========================LAUNCH========================= #
async def main():
    asyncio.create_task(daily_date(bot))
    asyncio.create_task(clear_daily_list())

    print("Bot is RUN....")
    
    # Очищаем очередь накопившихся сообщений
    await bot.delete_webhook(drop_pending_updates=True)

    #Launch Main commands to list in tg
    # await set_main_commands(bot)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())