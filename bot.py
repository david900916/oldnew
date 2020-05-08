
from discord.ext import commands

bot = commands.Bot(commands_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('NzA3OTA4Nzg4NzU3MjAwOTE2.XrPpkA.bbtF6vMMN9G0FN32TKL1xQ7_qOI')