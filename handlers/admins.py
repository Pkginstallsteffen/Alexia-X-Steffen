from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command(["pause", "rukja"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("» 😡😡 track paused by {} 𝐩𝐚𝐮𝐬𝐞 𝐤𝐢𝐮 𝐤𝐢𝐲𝐚𝐚 𝐛𝐞𝐞𝐞 𝐜𝐡𝐚𝐢𝐧 𝐬𝐞 𝐬𝐮𝐧𝐞𝐞𝐞𝐞 𝐭𝐨 𝐝𝐨 𝐤𝐚𝐦𝐬𝐞𝐤𝐚𝐚𝐚𝐦🥺".format( message.from_user.mention ), )


@Client.on_message(command(["resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("» 𝐡𝐚𝐲𝐞𝐞𝐞 𝐭𝐫𝐚𝐜𝐤 𝐫𝐞𝐬𝐮𝐦𝐞𝐝 𝐛𝐲 {} 𝐣𝐚𝐧𝐮𝐮𝐮😉".format( message.from_user.mention ), )


@Client.on_message(command(["end", " stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await message.delete()
    await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("» 𝐰𝐚𝐚𝐚𝐚𝐡 𝐰𝐚𝐚𝐚𝐚𝐚𝐡 😒 ;  𝐟𝐢𝐧𝐚𝐥𝐥𝐲 𝐒𝐭𝐫𝐞𝐚𝐦 𝐞𝐧𝐝𝐞𝐝 𝐛𝐲 {} 𝐛𝐨𝐥𝐮𝐮 𝐬𝐭𝐞𝐟𝐟𝐞𝐧 𝐤𝐨 𝐛𝐢𝐧𝐚 𝐩𝐮𝐜𝐡𝐞 𝐬𝐭𝐫𝐞𝐚𝐦 𝐞𝐧𝐝 𝐤𝐫𝐭𝐚𝐚 𝐡 𝐛𝐞𝐞𝐞😡".format(
      message.from_user.mention ), )

@Client.on_message(command(["skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    await message.delete()
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("» 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 𝐢𝐬 𝐩𝐥𝐚𝐲𝐢𝐧𝐠 𝐡𝐞𝐫𝐞😒 𝐭𝐡𝐞𝐧 𝐰𝐡𝐚𝐭 𝐭𝐨 𝐬𝐤𝐢𝐩 𝐡𝐮𝐮𝐮 𝐛𝐨𝐥𝐨 𝐝𝐢𝐤𝐡𝐭𝐚 𝐛𝐡𝐢 𝐧𝐚𝐡𝐢 𝐡 𝐤𝐲𝐚𝐚😒")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    await message.reply_text("» 𝐭𝐫𝐚𝐜𝐤 𝐬𝐤𝐢𝐩𝐩𝐞𝐝 𝐛𝐲 🥺 {} 𝐛𝐤𝐤 𝐞𝐤 𝐬𝐨𝐧𝐠 𝐬𝐮𝐧 𝐭𝐨 𝐩𝐭𝐚𝐚 𝐧𝐚𝐡𝐢 𝐡 𝐛𝐬𝐬 𝐬𝐤𝐢𝐩 𝐤𝐫𝐧𝐚𝐚 𝐡 😒".format( message.from_user.mention ), )
