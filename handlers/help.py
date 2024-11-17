
from pyrogram import Client, filters

async def help(client, message):
    await message.reply("Send a stock name or ticker symbol to get its current price and recommendations.")

handler = filters.command("help")(help)
