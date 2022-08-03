import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**🌈 ʜɪᴇᴇ ᴊᴀᴀɴ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), Aɴ ᴀᴅᴠᴀɴᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ😍


┏━━━━━━━━━━━━━━━
┣Ⓒⓡⓔⓐⓣⓔⓓ ⓑⓨ: [@STEFFEN999]
┣6𝘁𝗵-𝗚𝗲𝗻 𝗶𝗻𝗯𝘂𝗶𝗹𝘁 𝘀𝘆𝘀𝘁𝗲𝗺😍
┣༒︎𝗛𝗶𝘁𝗲𝗰𝗵 𝗘𝗻𝗴𝗶𝗻𝗲༒︎
┣💞𝐋𝐚𝐠 𝐟𝐫𝐞𝐞 & 𝐮𝐥𝐭𝐫𝐚 𝐪𝐮𝐚𝐥𝐢𝐭𝐲💞
┣🎯𝗠𝗼𝗿𝗲 𝗳𝗲𝗮𝘂𝘁𝘂𝗿𝗲𝘀 𝘀𝗼𝗼𝗻🎯
┣𝗕𝗲𝗰𝗼𝗺𝗲 𝗩𝗶𝗽 𝘂𝘀𝗲𝗿 & 𝘁𝗼 𝗴𝗲𝘁 𝗲𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗳𝗲𝗮𝘂𝘁𝘂𝗿𝗲𝘀 
 𝗹𝗶𝗸𝗲 𝗶𝗴 𝗳𝗼𝗹𝗹𝘄𝗲𝗿𝘀,𝗺𝗲𝗺𝗯𝗲𝗿 𝗮𝗱𝗱𝗶𝗻𝗴 𝘀𝗰𝗿𝗶𝗽𝘁
 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗧𝗦𝗛 𝗰𝗹𝗮𝗻 - @TSH_CLAN_ORG
┣ 🌈𝗧𝘆𝘀𝗺 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝘂𝘀 !!!
┗━━━━━━━━━━━━━━━

🌈 ꜰᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs ᴅᴍ @STEFFEN999 💦**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 ᴀᴅᴅ ᴋʀᴏ ɴᴀ ʙᴀʙʏ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👑 ᴏᴡɴᴇʀ 👑", url="https://t.me/STEFFEN999"
                    ),
                    InlineKeyboardButton(
                        "🍒 sᴜᴘᴘᴏʀᴛ 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "💦 ᴛsʜ ᴄʟᴀɴ 💦", url= "https://t.me/TSH_CLAN_ORG"
                    ),
                    InlineKeyboardButton(
                        "🎾 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🎾", url="https://github.com/Pkginstallsteffen/Alexia-X-Steffen"
                    )]
            ]
       ),
    )

