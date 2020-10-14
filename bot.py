# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()
trigger_words = ['im ', 'i\'m ']

@client.event
async def on_message(message):
    index = detect_im(message.content.lower())
    if index >= 0:
        await message.channel.send('hi ' + message.content[index:])

def detect_im(message):
    for trigger_word in trigger_words:
        response = detect(message, trigger_word, 0)
        if response >= 0:
            return response
    return -1

def detect(message, keyword, curr):
    index = message.find(keyword, curr)
    if index < 0:
        return -1
    if index == 0 or message[index-1] == ' ':
        return index+len(keyword)
    else:
        return detect(message, keyword, index+len(keyword))

client.run(token)

