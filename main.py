
from pyrogram import Client, filters
from handlers import start, help, stock_query

# Load environment variables
import config

# Initialize bot
app = Client("stock_bot", bot_token=config.BOT_TOKEN)

# Register handlers
app.add_handler(start.handler)
app.add_handler(help.handler)
app.add_handler(stock_query.handler)

# Run bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run()
