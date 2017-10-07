import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    try:
        if str(message.author) == 'JeydinNewWon#4863':
            val = message.content
            chan = message.channel
            if len(message.embeds) == 0:
                await client.delete_message(message)
                em = discord.Embed(colour=discord.Colour(16715599))
                em = em.set_author(name=client.user, icon_url=client.user.avatar_url)
                em = em.add_field(name='\u200b', value=val, inline=True)

                await client.send_message(chan, embed=em)

            else:
                return
    except discord.errors:
        pass
client.run('mfa.TUQVZ71aekMXwdve4KNFw5wXcDPzZR0Xs2qlV0UugoheyoVEzzqdvHvfHJgNpDZHS1A_2sA9IOBvE0lcKdx4', bot=False)
