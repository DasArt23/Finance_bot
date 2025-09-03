from aiogram import types
from defs.buttons import get_periods

async def month_report(message: types.Message):
    await message.answer("За какой промежуток времени вы хотите получить отчёт?", 
        reply_markup=get_periods())

async def automatic_report(message: types.Message):
    await message.answer("Выберите, как часто вы хотите получать автоматический отчёт")

async def add_expenses(message: types.Message):
    await message.answer("Какие затраты вы хотите добавить")

async def add_income(message: types.Message):
    await message.answer("Какие доходы вы хотите добавить")
