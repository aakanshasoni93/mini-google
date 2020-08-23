import dao.history_dao as history
from discord.ext import commands
import requests

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.history = history.History()
        self.use_db = True

    @commands.command(name='google', help='Do a google search')
    async def google_search(self, ctx, query=""):
        api_key = 'AIzaSyB9e1Sg-ul17eaLOZirMRoSKEE0FD_c50A'
        cx = '3ac7899905fa4f8d0'
        user = ctx.message.author
        if query == "" :
            await ctx.send("Please provide the string to query. for example: !google <query string>")
            return
        if self.use_db:
            self.history.save_history(user, query)

        params = {}
        params['key'] = api_key
        params['cx'] = cx
        params['q'] = query
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        result = response.json()['items']
        item_links = ""
        for i in range(5) :
            item_links = item_links + "\n" + str(result[i]['link'])
        await ctx.send(item_links)

    @commands.command(name='recent', help='search through history')
    async def recent_search(self, ctx, query=""):
        user = ctx.message.author
        if query == "" :
            await ctx.send("Please provide the string to query. for example: !recent <query string>")
            return
        if self.use_db:
            recent_searches = self.history.get_history(user, query)
        else:
            return
        if not recent_searches:
            await ctx.send("No results found")
        else:
            await ctx.send(recent_searches)

def setup(bot):
    bot.add_cog(Search(bot))
    print('Search bot loaded.')