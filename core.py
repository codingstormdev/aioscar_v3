import asyncio
import logging
import datetime
import platform
import pythonping

from aiogram import *
from aiogram.types import *
from aiogram.exceptions import *
from aiogram.filters import *

from datetime import *
from methods.main import *
from cfg import *

logger = logging.getLogger(__name__)

StartTime = datetime.now()
bot = Bot(botToken, parse_mode="HTML")
dp = Dispatcher()
router = Router()

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

@router.message(Command(commands=["status"]))
async def status(message: Message) -> None:
    await message.reply(
            f"Build:<code> {version}</code>" +
            f"\nCodename:<code> {codename}</code>" +
            f"\nUptime:<code> {str(datetime.now() - StartTime)}</code>" +
            f"\nChat id:<code> {str(message.chat.id)}</code>" +
            f"\nUser id:<code> {str(message.from_user.id)}</code>" +
            f"\nTelegram latency:<code> {str(pythonping.ping('api.telegram.org').rtt_avg_ms)}</code>" +
            f"\nLanguage:<code>Python {platform.python_version()}</code>" +
            f"\nLib:<code> aiogram 3</code>" +
            f"\nRunning system:<code> {platform.system()} {platform.release()}</code>" +
            f"\n@codingstorm, 2023")

async def coin(message: Message) -> None:
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())