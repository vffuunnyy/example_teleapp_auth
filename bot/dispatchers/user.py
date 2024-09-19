from telegrinder import (
    Dispatch,
    InlineButton,
    InlineKeyboard,
    Message,
)
from telegrinder.rules import Text
from telegrinder.types import MenuButtonWebApp, WebAppInfo

from bot.config import HOST


dp = Dispatch()
web_app = WebAppInfo(url=HOST)
web_app_keyboard = (
    InlineKeyboard()
    .add(
        InlineButton(
            "Open me 🐍",
            web_app=web_app,
        )
    )
    .get_markup()
)
chat_menu_button = MenuButtonWebApp(
    type="web_app",
    text="Open me 🐍",
    web_app=web_app,
)


@dp.message(Text("/start"))
async def handle_start_command(message: Message) -> None:
    await message.api.set_chat_menu_button(message.chat.id, chat_menu_button)
    await message.answer(
        "Open it!!!",
        reply_markup=web_app_keyboard,
    )
