import sqlite3

from aiogram import *
from aiogram.types import *
from aiogram.exceptions import *
from aiogram.filters import *

from cfg import *
from core import bot

async def isRoot(message) -> None:
    if message.from_user.id in rootID:
        return True
    

async def isAdmin(message) -> None:
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.status in ["administrator", "creator"]:
        return True
    

def isIgnored(message) -> None:
    with sqlite3.connect("config.db") as config:
        cfgdb = config.cursor()
        if cfgdb.execute("SELECT userid FROM ignoreuser WHERE userid = ?", (message.from_user.id,)).fetchone() != None or cfgdb.execute("SELECT chatid FROM ignorechat WHERE chatid = ?", (message.chat.id,)).fetchone() != None:
            userignored = cfgdb.execute("SELECT userid FROM ignoreuser WHERE userid = ?", (message.from_user.id,)).fetchone()[0]
            chatignored = cfgdb.execute("SELECT chatid FROM ignorechat WHERE chatid = ?", (message.chat.id,)).fetchone()[0]
            if message.chat.id == chatignored or message.from_user.id == userignored:
                return True
        
            
        
def isPrivate(message) -> None:
    if message.chat.type == "private":
        return True


async def isBotPromoted(message) -> None:
    member = await bot.get_chat_member(message.chat.id, bot.id)
    if member.status in ["administrator", "creator"]:
        return True