# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
😍 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʜᴇʏ...! ɴᴇɴᴜ ᴍᴇ ʙᴏᴛ ɴɪ 😁 ɴᴇɴᴜ ᴠᴄ ʟᴏ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴘʟᴀʏ ᴄʜᴇᴛʜᴀ ɴᴀɴᴜ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ....!**

😘 **ᴍᴇʀɪ ᴄᴏᴍᴍᴀɴᴅs ᴋɪɴᴅʜᴀ ᴄʜᴜᴅᴀᴠᴀᴄʜᴜ sɪᴍᴘʟᴇ ɢᴀ...» 😊 🅲🅾🅼🅼🅰🅽🅳🆂 ᴇ ʙᴜᴛᴛᴏɴ ᴜsᴇ ᴄʜᴇʏᴀɴᴅɪ!**

🤓 **ɴᴇᴋᴜ ᴛᴇʟᴜsᴀ ɴᴀ ʙᴏᴛ ɴɪ ᴇʟᴀ ᴜsᴇ ᴄʜᴇʏᴀʟᴏ ᴛᴇʟɪʏᴀᴘᴏᴛʜᴇ ᴋɪɴᴅʜs ᴇ ʙᴜᴛᴛᴏɴ ᴄʟɪᴄᴋ ᴄʜᴇʏᴀɴᴅɪ» 🙃 🅱🅰🆂🅸🅲 🅶🆄🅸🅳🅴 🅱🆄🆃🆃🅾🅽 ɴɪ ᴜsᴇ ᴄʜᴇsɪ ɴᴀɴᴜ ᴇssᴀʏ ɢᴀ ᴍᴀɴᴀɢᴇ ᴄʜᴇʏᴀɴᴅɪ 😁!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😉 ɴᴀɴᴜ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ 😁",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("🙃 Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("😊 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmds"),
                    InlineKeyboardButton("🥰 sᴀɴᴛʜᴏsʜ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "😁 sᴀɴᴛʜᴜ ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "😇 sᴀɴᴛʜᴜ Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "😘 Source Code", url="https://t.me/santhuvc"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""😒 ᴀʀᴇʏ ɴɪʙʙᴀ ᴋɪɴᴅʜᴀ ᴄʜᴜᴅᴜ ᴇʟᴀ ᴜsᴇ ᴄʜᴇʏᴀʟᴏ?, ᴍᴀᴅᴇ ʙʏ: @santhu_music_bot!
https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her (unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`).
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

😘 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

😊 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👈 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😜 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🥰 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("😊 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("👈 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""🛠 here is the basic commands:

» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /speedtest - run the bot server speedtest
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👈 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""🛠 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👈 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""🛠 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👈 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Settings of** {chat}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()
