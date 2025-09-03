from aiogram import types

async def test1(message: types.Message):
    await message.reply("Test 1")

async def test2(message: types.Message):
    await message.reply("Test 2")
