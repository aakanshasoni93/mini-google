from discord.ext import commands
TOKEN = "************************"
bot = commands.Bot(command_prefix='!')
cogs = ["cogs.events", "cogs.search"]
for cog in cogs:
    bot.load_extension(cog)
bot.run(TOKEN)