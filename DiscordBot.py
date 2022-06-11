from dotenv import load_dotenv
import os
import discord

load_dotenv()
TOKEN = os.environ["disc_token"]
connected = False

client = discord.Client()

@client.event
async def on_connect():
    connected = True