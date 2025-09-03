from aiogram import types
from defs.buttons import *

async def start(message: types.Message):
    await message.answer("Открыто меню", reply_markup=get_menu_buttons())

async def help_inf(message: types.Message):
    await message.answer("Это должна быть памятка")    
