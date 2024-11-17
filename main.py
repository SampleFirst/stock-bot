from pyrogram import Client
import config
import handlers.start  # Import start handler to ensure it registers
import handlers.help  # Import help handler
import handlers.stock_query  # Import stock query handler

# Initialize the bot
app = Client(
    "stock_bot",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
)

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run()
