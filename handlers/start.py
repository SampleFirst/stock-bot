
from pyrogram import Client, filters

async def start(client, message):
    await message.reply("Welcome to Stock Bot! Send me a stock name to get its report.")

handler = filters.command("start")(start)
