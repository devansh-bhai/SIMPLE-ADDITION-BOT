from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os


bot = Client("bot",
             bot_token= "5067758600:AAFb0WIHF96XqYF3pNav0jQFWGdhd0hkKTU", 
             api_id= 28590119, #api
             api_hash= "2494557bf21e6c5152f26070aa1a97c7")


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/ITS_NOT_ROMEO",
            ),
            InlineKeyboardButton(
                text="❣️ GITHUB",
                url="https://github.com/Devansh20055",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Main Channel",
                url="https://t.me/TEAM_SILENT_KING_OG",
            ),
            
        ],
    ]
)


@bot.on_message(filters.command(["start"]))
async def STRT(bot: Client, m: Message):
    editable = await m.reply_text(f"**➠ HI ! I AM ADDITION BOT  **",reply_markup=keyboard)
     
@bot.on_message(filters.command(["add"]))
async def add(bot: Client, m: Message):
    editable = await m.reply_text(f"**➠ SEND 1ST NO TO ADD **")
    input: Message = await bot.listen(editable.chat.id)
    raw_text0 = input.text
    editable = await m.reply_text(f"**➠ SEND 2ND NUMBER **")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1 = input1.text
    ADDIND = int(raw_text0)+int(raw_text1)
    #ADDIND = raw_text0+raw_text1
    await m.reply_text(f"**Addition is : {ADDIND} \n BOT BY @ITS _NOT _ROMEO ON TG **")
     
bot.run()
