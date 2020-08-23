from discord.ext import commands
TOKEN = "NzQ2MzkzMTYyMTkyMjU3MTk2.Xz_qzQ.VOrh0naN59P2Mun-KL36_aEmfbA"
bot = commands.Bot(command_prefix='!')
cogs = ["cogs.events", "cogs.search"]
for cog in cogs:
    bot.load_extension(cog)
bot.run(TOKEN)