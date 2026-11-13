from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

from configur import ADMIN
from datebase import datebase

AD = ADMIN
db = datebase
router = Router()

@router.callback_query(F.data == '/remove')
async def remove_person(callback: CallbackQuery):
    
    if not isinstance(callback.message , Message):
        await callback.answer('the Message is not available',
            show_alert=True)
        return
        
    message_text = callback.message.text
    chat_id = callback.message.chat.id
    name = None
    surname = None
    date = None

#"<b>Имя:</b> {name}\n<b>Фамилия:</b> {surname}\n<b>Дата рождения:</b> {str_date}-{str_year}\n"
    
    if( not message_text):
        return
    arr_text = message_text.split("\n")
    del arr_text[0]

    for len in arr_text :
        arr_info = len.split('</b>')
        if("<b>Имя:" in arr_info[0]):
            name = arr_info[1].strip()
        elif("<b>Дата рождения:" in arr_info[0]):
            date_arr = arr_info[1].strip().split('-')
            date = (f"{date_arr[0]}-{date_arr[1]}", f"{date_arr[2]}")
        elif("<b>Фамилия:" in arr_info[0]):
            surname = arr_info[1].strip()
    if (name and surname and chat_id):
        del db[chat_id][(name , surname)]

    
    

  
    