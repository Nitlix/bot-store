import asyncio

from discord.message import Attachment
import discord
import json
import threading
import os
import captcha
import storage as io
import uuid
from discord.ext import commands

main = {
    "games":[],
    "channels":{}

    }









intents1 = discord.Intents.default()
intents1.members = True
client = discord.Client(intents=intents1)
from captcha.image import ImageCaptcha
import random, string



@client.event
async def on_ready():
  print("Squid Game Successfuly launched.")
  print("Logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.Game(name=f"> sg!help"))






@client.event
async def on_message(msgu):
  if str(msgu.channel.type) != 'private':


    



@client.event
async def on_guild_join(guild):
  if guild.get_member(904008543055777792).guild_permissions.administrator:
    titl = f'Hi, {guild.owner.name}! Thanks for adding me to **{guild.name}**!'
    desc = f"I am glad you wanted to use me to play squid game, {guild.owner.mention}! :) \n\nPlease make sure there are no guns on you, you don't truly die in this game! ;)"
    personalEmbed = discord.Embed(title=titl, description=desc, color=3997951)
    personalEmbed.set_thumbnail(url=guild.icon_url)
    personalEmbed.set_image(url="https://raw.githubusercontent.com/Nitlix/bot-store/main/Nitlix%20Studios/Utils/thanks_for_adding.png")
    dm = await guild.owner.create_dm()
    await dm.send(embed=personalEmbed)
    
    await dm.send("Created the config! You can start using me now! :D")
    

client.run('OTA0MDA4NTQzMDU1Nzc3Nzky.YX1RkA.pBqTeNAXmDsaxqU6WbmkSJiYMsM')