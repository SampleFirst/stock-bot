from pyrogram import Client
from aiohttp import web
from handlers.web_server import create_web_server
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
        print(f"Bot {me.username} is running...")

        # Start the web server
        web_app = create_web_server()
        runner = web.AppRunner(web_app)
        await runner.setup()
        bind_address = "0.0.0.0"
        site = web.TCPSite(runner, bind_address, config.PORT)
        await site.start()
        print(f"Web server running on {bind_address}:{config.PORT}")

    async def stop(self, *args):
        print("Bot is stopping...")
        await super().stop()

# Run the bot
if __name__ == "__main__":
    app = StockBot()
    app.run()
