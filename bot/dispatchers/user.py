from telegrinder import (
    Dispatch,
    InlineButton,
    InlineKeyboard,
    Message,
)
from telegrinder.rules import Text
from telegrinder.types import WebAppInfo

from bot.config import HOST


dp = Dispatch()
kb = (
    InlineKeyboard()
    .add(
        InlineButton(
            "Open me 🐍",
            web_app=WebAppInfo(url=HOST),
        )
    )
    .get_markup()
)


@dp.message(Text("/start"))
async def handle_start_command(message: Message) -> None:
    await message.answer(
        "Open it!!!",
        reply_markup=kb,
    )
