import discord
from discord.ext import commands

TOKEN = "NzQ5MzA4ODQ1MjYzNjgzNjI1.GZem7n.CxVzuBiLulXxWuX86Y_zJ6Fh5fQzv_LsJpzKnA"
KEYWORDS = ["Ukraine", "ukraine"]  # Words to detect
REPLY_TEXT = "HАШ Слава Богу 🙏❤️СЛАВА РОССИИ 🙏❤️АНГЕЛА ХРАНИТЕЛЯ КАЖДОМУ ИЗ ВАС 🙏❤️БОЖЕ ХРАНИ РОССИЮ 🙏❤️СПАСИБО ВАМ НАШИ МАЛЬЧИКИ 🙏🏼❤️🇷🇺 ЧТО ПОДДЕРЖИМ НАШИХ СРАЗУ видно НАШ СЛОНЯРА🇷🇺🇷🇺💪 СВО слава тебе Господи🇷🇺🇷🇺🇷🇺💪🔥🔥 СВО да хранит ТЕБЯ ГОСПОДЬ🔥💪💪🇷🇺 НАШ живчик СРАЗУ видно НАШИХ парней издалека🇷🇺🇷🇺🇷🇺🇷🇺💪💪💪💪💪 СВОих не бросаем🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺🇷🇺💪💪Слава Богу СВО🙏❤️СЛАВА СВО🙏❤️АНГЕЛА ХРАНИТЕЛЯ СВО КАЖДОМУ ИЗ ВАС🙏❤️БОЖЕ ХРАНИ СВО🙏❤️СПАСИБО ВАМ НАШИ СВО🙏🏼❤️🇷🇺 ХРОНИ СВО✊🇷🇺💯СПАСИБО ВАМ НАШИ МАЛЬЧИКИ 🙏🏼❤️🇷🇺 ЧТО ПОДДЕРЖИВАЕТЕ СВО"
bot_enabled = True  # Toggle state

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
@commands.has_permissions(administrator=True)
async def toggle(ctx):
    global bot_enabled
    bot_enabled = not bot_enabled
    await ctx.send(f"Bot is now {'ON' if bot_enabled else 'OFF'}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot_enabled:
        if any(word in message.content.lower() for word in KEYWORDS):
            await message.channel.send(REPLY_TEXT)

    await bot.process_commands(message)  # Ensures commands still work

bot.run(TOKEN)
