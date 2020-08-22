import discord
from discord.ext import commands
import requests
TOKEN = "NzQ2MzkzMTYyMTkyMjU3MTk2.Xz_qzQ.bBttkLEqF8hZTB07jv0jTcWGB5s"
client = discord.client()
client = commands.Bot(command_prefix='!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'hi' in message.content.lower() :
        response = "Hey {} !!".format(message.author)
        await message.channel.send(response)
    await client.process_commands(message)
api_key = 'AIzaSyB9e1Sg-ul17eaLOZirMRoSKEE0FD_c50A'
cx = '3ac7899905fa4f8d0'
@client.command(name='google', help='Do a google search')
async def google_search(ctx, query=""):
    if query == "" :
        await ctx.send("Please provide the string to query. for example: !google <query string>")
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
client.run(TOKEN)