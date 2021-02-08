import discord
import random

client = discord.Client()
token = "NTYyNzE0MzgyMDgxOTgyNTA0.XKOymw.Fv8n-N82TJYXm6XjBRSkTzkrUTs"

lesh = "https://sun9-52.userapi.com/impf/4KWXqPx0evBJp2IKkgQwjtYrH9FHcygsqNjOfA/zWrVksgkSHU.jpg?size=206x44&quality=96&proxy=1&sign=6925a68407891d6142060db5d451d31e&type=album"
koleno = "https://sun9-62.userapi.com/impf/n0Ggky9GrNZZ8_auObFP_E_7kJ132mBLxYKhNA/LPRHcjKTHNs.jpg?size=210x41&quality=96&proxy=1&sign=fd2c4901421f5e6e2c1cf6985ba4d897&type=album"
slomanyylesh = "https://media.discordapp.net/attachments/473118213371199489/808296627868663818/82cc9ad7f6b58064.jpg"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('И че с тобой делать?'):
        y = random.randint(0, 99)
        if (y == 88):
            await message.channel.send(slomanyylesh)
        else:
            x = random.randint(0, 1)
            if (x == 0):
                await message.channel.send(lesh)
                #await message.channel.send(x)
            else:
                await message.channel.send(koleno)
                #await message.channel.send(x)

client.run(token)