import json
import traceback
from threading import Thread

import discord
import time
from telegram import Bot

with open('services.json') as file:
    config = json.load(file)
    discord_bot_token = config['discord']['reveal_token']
    channel = config['discord']['channel']
    telegram_bot_token = config['telegram']['bot_token']
    telegram_chat_id = config['telegram']['chat_id']

client = discord.Client()

bot = Bot(telegram_bot_token)

"""
    Check each new msg of users
"""
@client.event
async def on_message(message):
    """ If this msg from the specified channel"""
    if channel in str(message.channel):
        # Skip bot msg
        if message.author == client.user:
            return

        if message:
            print(message.content)
            msg = '<b>Discord Message</b> From <b>%s</b> Channel: #general:\n%s' % (
                message.author.display_name, message.content)
            bot.send_message(telegram_chat_id,
                             msg,
                             parse_mode='HTML')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(discord_bot_token)
