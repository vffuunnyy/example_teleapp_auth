from envparse import env


HOST = env.str("HOST")
PORT = env.int("PORT")
WEBHOOK_PATH = env.str("WEBHOOK_PATH")
WEBHOOK_URL = HOST + WEBHOOK_PATH
BOT_TOKEN = env.str("BOT_TOKEN")
