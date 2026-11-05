from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from configur import ADMIN as AD
from datebase import datebase as dt
from saver import async_save_congratulations, congrat

database = dt
router = Router()
ADMIN = AD



@router.message(Command("gift"))
async def gift_writing(message: Message):
    
    if not message.text : #Проверка на существование текста 
        await message.answer(
            text= "<b>Введите пожалуйста команду текстом.</b>\n" 
            "Пример: <blockquote>/gift Поздравляю тебя {name}</blockquote>" , 
            parse_mode= "HTML")
        return

    text_arr = message.text.split(maxsplit=1)

    if len(text_arr) < 2:
        await message.answer(
            "<b>Неверный формат!</b>\n"
            "Используйте: <code>/gift text</code>\n"
            "<i><b>Пример</b>: <blockquote>/gift Hello {name}! Happy birthday!</blockquote></i>",
            parse_mode="HTML"
        )
        return

    congratulation_text = text_arr[1]
    
    congrat.append(congratulation_text)
        
    await async_save_congratulations()
    
    await message.answer(
            "<b>Поздравление успешно добавлено!</b>\n\n"
            "<b><i>Текст:</i></b> \n"
            f"<blockquote>{congratulation_text}</blockquote>",
            parse_mode="HTML"
        )
