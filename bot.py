import discord
import asyncio

client = discord.Client()

f = open('configs.txt')
user_info = []
for line in f:
    pure_line = line.rstrip()
    x, y = pure_line.split(':')
    user_info.append(y)

token = user_info[0]
username = user_info[1]
colour = user_info[2]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    try:
        if str(message.author) == username:
            val = message.content
            chan = message.channel
            if len(message.embeds) == 0:
                await client.delete_message(message)
                em = discord.Embed(colour=colour)
                em = em.set_author(name=client.user, icon_url=client.user.avatar_url)
                em = em.add_field(name='\u200b', value=val, inline=True)

                await client.send_message(chan, embed=em)

            else:
                return
    except discord.errors:
        pass
client.run(token, bot=False)
