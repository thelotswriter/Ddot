import os
import random
import discord
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(messages=True, guilds=True)
client = commands.Bot(command_prefix='!', intents=intents)
messages = ['Boo <@!1026624616552218684>!',
            'Go away <@!1026624616552218684>!',
            'Not again, <@!1026624616552218684>.',
            'I hate you <@!1026624616552218684>.']
gifs = ['https://tenor.com/view/awesomeness-tv-you-tube-shut-up-quiet-shush-zip-gif-8937690',
        'https://tenor.com/view/chandler-bing-shut-up-scream-gif-15560691',
        'https://tenor.com/view/go-away-lion-king-kids-bye-throw-gif-12600764',
        'https://tenor.com/view/go-away-homer-simpson-gif-14732129',
        'https://tenor.com/view/spongebob-squarepants-get-out-kick-out-booted-bye-felicia-gif-13565963']


def generate_insult(choice=random.random):
    choice = random.random()
    if choice < 0.75:
        if choice < 0.25:
            index = 0
        elif choice < 0.5:
            index = 1
        elif choice < 0.6:
            index = 2
        else:
            index = 3
        return messages[index]
    else:
        if choice < 0.8:
            index = 0
        elif choice < 0.85:
            index = 1
        elif choice < 0.9:
            index = 2
        elif choice < 0.95:
            index = 3
        else:
            index = 4
        return gifs[index]


@client.event
async def on_message(message):
    txt = message.content
    channel = message.channel
    author = message.author
    if str(author) == 'CaptianCaption#6344' and str(channel) != 'bot-nonsense':
        await channel.send(generate_insult(choice=random.random()))
    await client.process_commands(message)

client.run(token)
