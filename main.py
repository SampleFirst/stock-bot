from pyrogram import Client
import config

app = Client(
    "stock_bot",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
