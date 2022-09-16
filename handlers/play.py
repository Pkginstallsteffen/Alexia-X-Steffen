import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, SUPPORT_GROUP
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(
    command(["play", "p", "fuck"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    await message.delete()

    fallen = await message.reply("» ᴘʀᴏᴄᴇssɪɴɢ​... ᴛʜᴏᴅᴀ ᴡᴀɪᴛ ᴋʀ ʟᴏ ɴᴀ ᴊᴀᴀɴ🔎")

    chumtiya = message.from_user.mention

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Steffen"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await fallen.edit(
                        "<b>» 𝐚𝐫𝐞𝐞𝐞 𝐣𝐚𝐚𝐚𝐧 𝐩𝐡𝐥𝐞𝐞 𝐦𝐞𝐤𝐨 𝐚𝐝𝐦𝐢𝐧 𝐛𝐚𝐧𝐚𝐚𝐨 𝐧𝐚𝐚 𝐢𝐭𝐧𝐚𝐚 𝐛𝐡𝐢 𝐧𝐚𝐡𝐢 𝐬𝐚𝐦𝐣𝐡𝐭𝐞𝐞 𝐤𝐚𝐢𝐬𝐞𝐞 𝐥𝐚𝐝𝐤𝐢 𝐤𝐨 𝐩𝐚𝐭𝐚𝐨𝐠𝐞𝐞 𝐡𝐮𝐮😂😒❤️ </b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "» 𝐈'𝐦 𝐣𝐨𝐢𝐧𝐞𝐝 𝐭𝐡𝐞 𝐜𝐡𝐚𝐭 𝐣𝐚𝐧𝐮𝐮 , 𝐧𝐨𝐰 𝐮 𝐜𝐚𝐧 𝐩𝐥𝐚𝐲 𝐲𝐨𝐮𝐫 𝐝𝐞𝐬𝐢𝐫𝐞𝐝 𝐬𝐨𝐧𝐠𝐬.. 𝐚𝐧𝐲 𝐪𝐮𝐞𝐫𝐢𝐞𝐬 𝐭𝐡𝐞𝐧 𝐝𝐦😉 @STEFFEN999.")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>» ᴀssɪsᴛᴀɴᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ʙᴀʙʏ, sᴇɴᴅ /join ғɪʀsᴛ ᴛɪᴍᴇ ᴛᴏ ᴏʀᴅᴇʀ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴊ​ᴏɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>» 𝐨𝐨 𝐡𝐞𝐥𝐥𝐨𝐨𝐨𝐨𝐨𝐨𝐨𝐨 𝐢'𝐦 𝐟𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐭𝐡𝐢𝐬 𝐜𝐡𝐚𝐭 😒😒.</i>\n\nʀᴇᴀsᴏɴ : {e}")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"» 𝐨𝐨𝐩𝐬 𝐬𝐨𝐫𝐫𝐲 𝐣𝐚𝐚𝐚𝐧𝐮🥺 𝐭𝐫𝐚𝐜𝐤 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 😛 {DURATION_LIMIT} 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐥𝐥𝐨𝐰𝐝𝐞𝐝 𝐭𝐨 𝐩𝐥𝐚𝐲.. 𝐮 𝐜𝐚𝐧 𝐩𝐥𝐚𝐲 𝐚𝐧𝐲 𝐬𝐨𝐧𝐠 𝐥𝐞𝐬𝐬 𝐨𝐫 𝐞𝐪𝐮𝐚𝐥 𝐭𝐨 120 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 😉😉"
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            title = "NaN"
            duration = "NaN"
            views = "NaN"

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"» 𝐨𝐨𝐩𝐬 𝐬𝐨𝐫𝐫𝐲 𝐣𝐚𝐚𝐚𝐧𝐮🥺 𝐭𝐫𝐚𝐜𝐤 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 😛 {DURATION_LIMIT} 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐥𝐥𝐨𝐰𝐝𝐞𝐝 𝐭𝐨 𝐩𝐥𝐚𝐲.. 𝐮 𝐜𝐚𝐧 𝐩𝐥𝐚𝐲 𝐚𝐧𝐲 𝐬𝐨𝐧𝐠 𝐥𝐞𝐬𝐬 𝐨𝐫 𝐞𝐪𝐮𝐚𝐥 𝐭𝐨 120 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 😉😉"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await fallen.edit(
                "» 𝐚𝐥𝐞𝐞𝐞 𝐦𝐞𝐫𝐚 𝐛𝐚𝐜𝐡𝐚𝐚 𝐛𝐢𝐧𝐚𝐚 "#𝐬𝐨𝐧𝐠_𝐧𝐚𝐦𝐞" 𝐤𝐚 𝐤𝐚𝐢𝐬𝐞𝐞 𝐩𝐥𝐚𝐲 𝐤𝐫𝐮𝐮𝐮😒 .. 𝐠𝐢𝐯𝐞 𝐬𝐨𝐦𝐞 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 𝐲𝐚𝐚𝐚𝐚𝐚𝐚𝐚𝐫😘 "
            )
        await fallen.edit("🔎")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await fallen.edit(
                "»ʙᴋᴋ ɴᴏᴛ ғᴏᴜɴᴅ ʏᴀʀʀ🥺, ᴋᴇᴇᴘ sᴇᴀʀᴄʜɪɴɢ ᴡɪᴅ ᴛʜᴇ sᴏɴɢ ɴᴀᴍᴇ ᴊᴀᴀᴀɴ🥺💞"
            )
            print(str(e))
            return

        if (dur / 60) > DURATION_LIMIT:
            await fallen.edit(
                f"» 𝐨𝐨𝐩𝐬 𝐬𝐨𝐫𝐫𝐲 𝐣𝐚𝐚𝐚𝐧𝐮🥺 𝐭𝐫𝐚𝐜𝐤 𝐥𝐨𝐧𝐠𝐞𝐫 𝐭𝐡𝐚𝐧 😛 {DURATION_LIMIT} 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐥𝐥𝐨𝐰𝐝𝐞𝐝 𝐭𝐨 𝐩𝐥𝐚𝐲.. 𝐮 𝐜𝐚𝐧 𝐩𝐥𝐚𝐲 𝐚𝐧𝐲 𝐬𝐨𝐧𝐠 𝐥𝐞𝐬𝐬 𝐨𝐫 𝐞𝐪𝐮𝐚𝐥 𝐭𝐨 120 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 😉😉 "
            )
            return
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_text(
            text=f"**» ᴛʀᴀᴄᴋ ǫᴜᴇᴜᴇᴅ ᴀᴛ {position} ᴊᴀɴɴᴜᴜ**\n📌 **ᴛɪᴛʟᴇ​ :**[{title[:65]}]({url})\n\n🕕** ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` **ᴍɪɴᴜᴛᴇs**\n💕** ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ​ : **{chumtiya}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• sᴜᴩᴩᴏʀᴛ •", url="https://t.me/we_love_eachother"),
                    InlineKeyboardButton("» ᴄʟᴏsᴇ «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_text(
            text=f"**ㅤㅤㅤ» 🎧ɴᴏᴡ ᴘʟᴀʏɪɴɢ ᴊᴀᴀɴ🎧 «**\n📌 **🎾Sᴏɴɢ ᴛɪᴛʟᴇ🎾​:** [{title[:65]}]({url})\n🕕 **🎈ᴅᴜʀᴀᴛɪᴏɴ🎈:** `{duration}` ᴍɪɴᴜᴛᴇs\n💕 **😍ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ😍​:** {chumtiya}\n💔 **ᴘʟᴀʏɪɴɢ ɪɴ​:** `{message.chat.title}`\n🎥 **sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** ʏᴏᴜᴛᴜʙᴇ ᴍᴜsɪᴄ\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😘sᴜᴩᴩᴏʀᴛ ᴊᴏɪɴ😘", url="https://t.me/we_love_eachother"),
                    InlineKeyboardButton("» 😘ᴄʟᴏsᴇ😘 «", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

    return await fallen.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
