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
    If bot is ready
"""
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    while True:
        try:
            # get new updates
            new_message = wait_new_message(bot)
            message = new_message.message \
                if new_message.message is not None \
                else new_message.callback_query.message

            # is it our chat
            _is_specified_chat = str(message.chat.id) in str(telegram_chat_id)
            if _is_specified_chat:
                # retrieve user msg
                text = str(get_action(new_message))
                first_name = message.from_user.first_name

                print(first_name)
                print(text)
                msg = '**Telegram Message** From **%s**:\n%s' % (
                    first_name, text)
                channel = get_discord_channel()
                print(channel)
                await client.send_message(channel, msg)
        except Exception as e:
            traceback.print_exc()
            print(e)


def get_discord_channel():
    channels = client.get_all_channels()
    for _channel in channels:
        if _channel.name == channel:
            return _channel
    return None


def wait_new_message(bot):
    while True:
        updates = bot.get_updates()
        if len(updates) > 0:
            break
        else:
            time.sleep(5)
    update = updates[0]
    bot.get_updates(offset=update["update_id"] + 1)
    return update


def get_action(message):
    if message['message'] is not None:
        menu_option = message['message']['text']
    elif message["callback_query"] != 0:
        menu_option = message["callback_query"]["data"]
    return menu_option


client.run(discord_bot_token)
