import discord
from discord.ext import commands
import os, random, asyncio, telegram_send

#variables
token = "OTI0MDEyOTM5MzM2Mzg0NTI0.YcYYHA.BDSc9zpiEnnvfv4rzxwng-sAAXI"
dailyCat = 915717908364140615
dailyCatTest = 933913839135780956
cuteCats = "C:/Users/ADRIAN/Desktop/TheDailyCat/cats"

#random file
random_filename = random.choice([
    x for x in os.listdir(cuteCats)
    if os.path.isfile(os.path.join(cuteCats, x))
])

client = commands.Bot(command_prefix = ":3 ")

#every day do this
async def send_daily():
    await client.wait_until_ready()
    channel = client.get_channel(dailyCatTest)
    while not client.is_closed():
        random_filename = random.choice([
            x for x in os.listdir(cuteCats)
            if os.path.isfile(os.path.join(cuteCats, x))
        ])
        file = discord.File("C:/Users/ADRIAN/Desktop/TheDailyCat/cats/"+random_filename)
        await channel.send(file=file, content="<@&915717948046463098> here is your cat")
        print('sent daily')
        telegram_send.send(messages=["Sent Daily"])
        await asyncio.sleep(86400)

client.loop.create_task(send_daily()) #make it loop

client.run(token) #run the bot