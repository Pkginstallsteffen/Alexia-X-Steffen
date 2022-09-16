from pyrogram import Client, errors
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from youtubesearchpython import VideosSearch


@Client.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="𝐨𝐲𝐲 𝐭𝐲𝐩𝐞 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐯𝐢𝐝𝐞𝐨 𝐧𝐚𝐦𝐞...!🍑",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=" ",
                switch_pm_parameter="𝐝𝐞𝐤𝐡𝐨𝐨 𝐞𝐫𝐫𝐨𝐫 𝐚𝐚𝐠𝐲𝐚𝐚 𝐧𝐚𝐚🥺 : 𝐛𝐡𝐤𝐤 𝐲𝐚𝐚𝐚𝐚𝐚𝐚𝐫 𝐬𝐞𝐚𝐫𝐜𝐡 𝐭𝐢𝐦𝐞 𝐨𝐮𝐭 😒",
            )
