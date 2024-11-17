from pyrogram import Client
from handlers import web_server
import config

class StockBot(Client):
    def __init__(self):
        super().__init__(
            name="stock_bot",
            bot_token=config.BOT_TOKEN,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            workers=50,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, config.PORT).start()
        print(f"Bot {me.username} is running...")

    async def stop(self, *args):
        await super().stop()
        print("Bot is stopping...")

# Run the bot
if __name__ == "__main__":
    app = StockBot()
    app.run()
