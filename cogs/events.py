from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        user = str(message.author)

        if message.content.lower() == 'hi':
            response = "Hey {} !!".format(user.split('#')[0])
            await message.channel.send(response)

def setup(bot):
    bot.add_cog(Events(bot))
    print('Events bot loaded.')