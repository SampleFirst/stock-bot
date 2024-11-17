
from pyrogram import Client, filters
from utils.stock_api import get_stock_report
from utils.db import save_query

async def stock_query(client, message):
    query = message.text.strip()
    if not query:
        await message.reply("Please send a valid stock name or ticker symbol.")
        return

    report = get_stock_report(query)
    if report:
        await message.reply(f"Stock Report for {query}:

{report}")
        save_query(message.chat.id, query)
    else:
        await message.reply("Sorry, I couldn't find details for that stock.")

handler = filters.text & filters.private & ~filters.command(["start", "help"])(stock_query)