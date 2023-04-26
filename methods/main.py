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
    pass


def isPrivate(message) -> None:
    if message.chat.type == "private":
        return True
    

def isUserPromoted(message) -> None:
    pass


def isBotPromoted(message) -> None:
    pass