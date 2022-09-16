import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only
from callsmusic.callsmusic import client as user


@Client.on_message(
    command(["join", "assistant", " userbotjoin"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "𝐲𝐞𝐞𝐞𝐞𝐞𝐞𝐞𝐞𝐞𝐞𝐡!!😘 𝐢 𝐡𝐚𝐯𝐞 𝐣𝐨𝐢𝐧𝐞𝐝 𝐭𝐡𝐢𝐬 𝐜𝐡𝐚𝐭 𝐣𝐚𝐧𝐮𝐮𝐮𝐮𝐮.​")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "𝐚𝐫𝐞𝐞𝐞 𝐢 𝐚𝐦 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐞𝐫𝐞𝐞𝐞𝐞😒 𝐭𝐨 𝐚𝐛 𝐤𝐲𝐚𝐚 𝐣𝐨𝐢𝐧 𝐤𝐫𝐰𝐚𝐨𝐨𝐠𝐞 𝐥𝐚𝐝𝐨𝐨 𝐩𝐞𝐝𝐚𝐚 𝐛𝐨𝐥𝐨 𝐰𝐨 𝐛𝐡𝐢 𝐜𝐡𝐚𝐢𝐲𝐞𝐞 𝐭𝐨𝐨😒🍑")
        return await user.send_message(chat_id, "𝐚𝐫𝐞𝐞𝐞 𝐢 𝐚𝐦 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐡𝐞𝐫𝐞𝐞𝐞𝐞😒 𝐭𝐨 𝐚𝐛 𝐤𝐲𝐚𝐚 𝐣𝐨𝐢𝐧 𝐤𝐫𝐰𝐚𝐨𝐨𝐠𝐞 𝐥𝐚𝐝𝐨𝐨 𝐩𝐞𝐝𝐚𝐚 𝐛𝐨𝐥𝐨 𝐰𝐨 𝐛𝐡𝐢 𝐜𝐡𝐚𝐢𝐲𝐞𝐞 𝐭𝐨𝐨😒🍑​")
