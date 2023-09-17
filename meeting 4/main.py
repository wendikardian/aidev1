
import discord
import random
from discord.ext.commands import Bot
# client = Bot(command_prefix="!", intents=discord.Intents.all())
# client = discord.Client(intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "angry", "hurting", "stressed"]

happy_words = ["happy", "glad", "joyfull", "satisfied", "blessed"]

encouragements = [
    "GO GO GO",
    "Hung in there",
    "You are a great person",
    "Come on ! you can do it",
    "Stay Strong"
]


happy_responses = [
    "There you go 👌",
    "Keep up the good work ✌️",
    "Good Luck 😂",
    "Good job :D",
    "Im so proud of you 😎"
]


songs = [
    "https://www.youtube.com/watch?v=e-ORhEE9VVg",
    "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "https://www.youtube.com/watch?v=wmGrZFw4fEY"
]

# client = discord.Client(intents=discord.Intents.default())

# async def on_ready():
#     print("We have loggen in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        await message.channel.send("Hello")
    elif message.content.startswith('!turu'):
        await message.channel.send('https://media.tenor.com/xBCIftNkf4wAAAAj/sleep.gif')
    elif message.content.startswith('!random song'):
        await message.channel.send(random.choice(songs))

    if any(word in message.content for word in sad_words):
        response = random.choice(encouragements)
        await message.channel.send(response)
    if any(word in message.content for word in happy_words):
        response = random.choice(happy_responses)
        await message.channel.send(response)

# client.run("OTg2NDcyMzI1NTIyMjU5OTg4.GP6blh.-8A8UycFh9B6fvokFDBaq_z85jWQmRR99bd_3w")
client.run("OTg2NDYzODI2OTEwMjU3MjIy.Ge6RP6.U_3C7IWWOi4GFuWRsv9hMvrIDY8iqLWOM2sI_E")