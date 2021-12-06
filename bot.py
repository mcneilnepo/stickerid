import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

Bot = Client(
    "StickerIdBot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
 
   
START_TEXT = """
Hai {},
Am Sticker id Finder Bot
I can Find I'd of an sticker. Just send me a sticker and reply it with /StickerId command i would provide its I'd. . 
"""
    
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code📕', url='https://Github.com/MR-JINN-OF-TG/Stickerid'), 
        InlineKeyboardButton('CHANNEL📕', url=f"https://telegram.me/{Config.CHANNEL}")
        ]]
    )

@Bot.on_message(filters.private & filters.command(["stickerid"]))
async def stickers(bot, message):
    if message.reply_to_message.sticker:
       await message.reply(f"Your Requested Sticker's ID is   * `{message.reply_to_message.sticker.file_id}` *", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")
   
Bot.run()
