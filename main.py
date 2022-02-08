import os
import discord
import twitter
from dotenv import load_dotenv
load_dotenv()

api = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'),
                  consumer_secret=os.getenv('CONSUMER_SECRET'),
                  access_token_key=os.getenv('ACCESS_TOKEN_KEY'),
                  access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

def post_tweet(message):
    api.PostUpdate(status=message)

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!sendTweet'):
        post_tweet(message.content)
        await message.channel.send('Message envoyer')

client.run(os.getenv('TOKEN'))