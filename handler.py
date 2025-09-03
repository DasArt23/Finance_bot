from defs import commands, but_reacs
from data import dp
from aiogram.filters.command import Command
from aiogram import F

def command_handler(commands):
    for command in commands:
        dp.message.register(command[0], Command(command[1]))
        #print(command[0], command)

def buttons_kb_handler(but_reacs):
    for reaction in but_reacs:
        dp.message.register(reaction[0], F.text.lower() == reaction[1])

command_handler(commands)
buttons_kb_handler(but_reacs)

