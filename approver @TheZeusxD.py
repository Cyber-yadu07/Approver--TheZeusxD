from pyrogram import Client, filters

BOT_TOKEN = # your bot token
API_ID = # your api id 
API_HASH = # your api hash

Bot = Client(
    "noob",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Kya Re Bsdk {update.from_user.mention}"
    )
@bot.on_chat_join_request(filters.channel)
async def _(bot, update):
    await client.approve_chat_join_request()

Bot.run()