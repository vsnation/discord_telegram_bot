## Manual to deploy bots on VPS

Firstly install required libraries: 
```pip install -r requirements.txt```


## Configuration of services.json
Please, configure services.json file using your own settings.
To get the next fields, create your own app and bot in this website https://discordapp.com/developers/applications/
Services.json Fields:
#### Discord
* client_id - id of discord app.
* client_secret - secret_id of discord_app
* reveal_token - token of your bot
* channel - channel that bot will monitor

#### Telegram
* chat_id - id of the group where users will see msgs from discord
* bot_token - this token you can get from Botfather bot in telegram

To Run bots use the following commands:

``` python3 telegram_bot.py ``` - this bot responsible for sending msgs from specified telegram group.

``` python3 discord_sync_app.py ``` - this bot responsible for sending msgs from specified discord channel

You need to create init scripts to implement constant work of this bots