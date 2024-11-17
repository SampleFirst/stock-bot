from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome to Stock Bot! Send me a stock name to get its report.")
