from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("Send a stock name or ticker symbol to get its current price and recommendations.")
