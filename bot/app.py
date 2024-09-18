import asyncio
import secrets

from blacksheep import Application, FromBytes, Request, Response
from telegrinder import API, Dispatch, HTMLFormatter, Token
from telegrinder.modules import logger
from telegrinder.types.objects import Update

from bot.api import router
from bot.config import BOT_TOKEN, WEBHOOK_PATH, WEBHOOK_URL
from bot.dispatchers import user


SECRET_TOKEN = secrets.token_urlsafe(128)
app = Application(router=router)
api = API(token=Token(BOT_TOKEN))
api.default_params["parse_mode"] = HTMLFormatter.PARSE_MODE


async def on_startup() -> None:
    logger.info("Skipping pending updates")
    if (await api.get_webhook_info()).unwrap().url:
        await api.delete_webhook()

    await api.delete_webhook(drop_pending_updates=True)


dp = Dispatch()
for handler in [user]:
    logger.debug("Loading handler {!r}. Views count: {}", handler, len(handler.dp.get_views()))
    dp.load(handler.dp)

logger.info("Starting web server")


@app.lifespan
async def lifespan() -> None:
    await on_startup()

    logger.info("Setting webhook")
    await api.set_webhook(WEBHOOK_URL, secret_token=SECRET_TOKEN)
    yield
    await api.delete_webhook(drop_pending_updates=True)


@app.router.post(WEBHOOK_PATH)
async def webhook_bot(request: Request, payload: FromBytes) -> Response:
    if request.headers.get_first(b"X-Telegram-Bot-Api-Secret-Token").decode() != SECRET_TOKEN:
        return Response(404)

    update = Update.from_bytes(payload.value)
    logger.debug("Webhook received update (update_id={})", update.update_id)

    asyncio.create_task(dp.feed(update, api))  # noqa: RUF006

    return Response(200)
