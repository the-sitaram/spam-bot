from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("spam") & filters.private | filters.group)
def spam(_, message):
    try:
        count = int(message.command[1])
        text = " ".join(message.command[2:])
        for _ in range(count):
            message.reply_text(text)
    except:
        message.reply("Usage: /spam <count> <message>")


app.run()
