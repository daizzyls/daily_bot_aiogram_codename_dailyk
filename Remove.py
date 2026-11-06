from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

from datebase import datebase
from configur import ADMIN

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

    
    if( not message_text):
        return
    arr_text = message_text.split(" ")

    del arr_text[0]

    
    

  
    