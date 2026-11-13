from aiogram import F, Router
from aiogram.enums.chat_type import ChatType
from aiogram.filters import Command
from aiogram.types import (
    KeyboardButton,
    KeyboardButtonRequestUsers,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

router = Router()

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(
    text="search user info",
    request_users=KeyboardButtonRequestUsers(
        request_id= 1,
        user_is_bot= False,
        max_quantity= 1,
        request_name= True,
        request_username= True,
        request_photo= True
    ),
    )],
],resize_keyboard=True)

@router.message(Command('myid') , F.chat.type == ChatType.PRIVATE)
async def get_my_telegram_information(mess : Message):
    if(mess.from_user):
        current_user = mess.from_user

    myusername = f"@{current_user.username}" if current_user.username else "none"
    
    text = (
        "<b>Your TG information:</b>\n"
        f"<blockquote><b>ID:</b> <code>{current_user.id}</code>\n"
        f"<b>F_name:</b> <i>{current_user.first_name}</i>\n"
        f"<b>L_name:</b> <i>{current_user.last_name if current_user.last_name else "none"}</i>\n"
        f"<b>Username:</b> <i>{myusername}</i>\n"
        f"<b>Lang:</b> <i>{current_user.language_code}</i>\n"
        f"<b>Premium:</b> <i>{'Yes' if current_user.is_premium else 'No'}</i></blockquote>"
    )
    
    await mess.answer(
        text=text,
        parse_mode="HTML",
        reply_markup=keyboard,
    )

@router.message(F.users_shared ,F.chat.type == ChatType.PRIVATE)
async def user_telegram_information(message : Message):
    if(message.users_shared):
        shared_user = message.users_shared.users[0]

    username = f"@{shared_user.username}" if shared_user.username else "none"

    text = (
        "<b>Information about your friend:</b>"
        f"<blockquote><b>F_name</b>: <i>{shared_user.first_name or "none"}</i>\n"
        f"<b>L_name</b>: <i>{shared_user.last_name or "none"}</i>\n"
        f"<b>Username:</b> <i>{username}</i>\n"
        f"<b>User_ID:</b> <code>{shared_user.user_id}</code></blockquote>"
    )

    if(shared_user.photo):
        await message.answer_photo(
            photo=shared_user.photo[-1].file_id,
            caption=text,
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove()
        )
    else :
        await message.answer(
            text=text,
            parse_mode='HTML',
            reply_markup=ReplyKeyboardRemove()
        )