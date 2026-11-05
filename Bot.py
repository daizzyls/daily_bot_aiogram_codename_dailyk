# =========================IMPORT========================= #
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import BotCommand, Message

from congratulations import congratulations
from datebase import datebase
from Datee import router as date_router
from Gift import router as gift_router
from Info import router as info_router
from strTOK import BOT_TOKEN

# 1. Импортируем фоновые задачи из вашего файла tasks.py
from tasks import clear_daily_list, daily_date
from today import congratulated_today

# =========================SETTINGS========================= #
TELEGRAM_TOKEN = BOT_TOKEN
ADMIN = '1054191711'

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(date_router)
dp.include_router(info_router)
dp.include_router(gift_router)

# =========================DataBase========================= #
database = datebase
congrat = congratulations
today_congratulated = congratulated_today

# =========================Keyboard========================= #
# async def set_main_commands(bot : Bot):
#     main_commands = [
#         BotCommand(command='start' , description='Restart bot and send greeting message'),
#         BotCommand(command='date' , description='<name> <surname> <data> - Set name, surname and date of birth in the database'),
#         BotCommand(command='gift' , description='<descr> - Write your own congratulation'),
#         BotCommand(command='info' , description='Show information, that you set in bot (by your status(Admin and...)'),
#     ]
#     await bot.set_my_commands(main_commands)

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