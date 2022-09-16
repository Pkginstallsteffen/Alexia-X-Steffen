import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME as bn
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["erase", "rmd"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    await message.delete()
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("**𝐎𝐮𝐫 𝐡𝐢𝐭𝐞𝐜𝐡 𝐬𝐲𝐬𝐭𝐞𝐦 𝐡𝐚𝐬 𝐝𝐞𝐥𝐞𝐭𝐞𝐝😙 𝐚𝐥𝐥 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐟𝐢𝐥𝐞𝐬 𝐟𝐫𝐨𝐦 {} 𝐨𝐮𝐫 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐣𝐚𝐧𝐮𝐮𝐮​**".format(bn) )
    else:
        await message.reply_text("**𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐧𝐨 𝐟𝐢𝐥𝐞𝐬 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐝 𝐨𝐧 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐛𝐚𝐛𝐲😉​**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    await message.delete()
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("**{} 𝐚𝐥𝐥 𝐫𝐚𝐰 𝐟𝐢𝐥𝐞𝐬 𝐚𝐫𝐞 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 **".format(bn) )
    else:
        await message.reply_text("**𝐍𝐨 𝐫𝐚𝐰 𝐟𝐢𝐥𝐞𝐝 𝐜𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐟𝐨𝐮𝐧𝐝🍑🍑​**")


@Client.on_message(command(["clear", " rmp"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    await message.delete()
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("**𝐂𝐥𝐞𝐚𝐧𝐞𝐝😉​**")
    else:
        await message.reply_text("**𝐂𝐥𝐞𝐚𝐧𝐞𝐝😉​**")
