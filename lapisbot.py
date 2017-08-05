import discord
from discord.ext.commands import Bot 
from discord.ext import commands 
import asyncio
import random

random.seed
 
Client = discord.Client()
bot_prefix= ">>"
client = commands.Bot(command_prefix=bot_prefix)



@client.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name='with water'))

@client.command(pass_context=True) 
async def lapis(ctx): 
	await client.say("lazuli")
	
@client.command(pass_context=True) 
async def my(ctx):
	out = random.choice(['this meme is fucking retarded', 'nama jeff'])
	await client.say(out)
	random.seed

@client.command(pass_context=True) 
async def goodanime(ctx):
	await client.say("none of them you fucking weeb")

@client.command(pass_context=True) 
async def goodvidya(ctx):
	out = random.choice(['Hotline Miami', 'Fallout: New Vegas', 'Max Payne', 'XCOM: Enemy Unknown', 'Dark Souls', 'Metal Gear Rising', 'Rimworld', 'Deus Ex: Human Revolution', 'One Way Heroics', 'Resident Evil: HD REmaster', 'FTL: Faster Than Light', 'Postal 2', 'Stardew Valley', 'Sleeping Dogs', 'Wolfenstien: The New Order', 'Always Sometimes Monsters'])
	await client.say(out)
	random.seed
	
@client.command(pass_context=True) 
async def commandlist(ctx):
	await client.say("Commands (case sensitive): \n **>>lapis**- Best Gem \n **>>my**- try and revive a dead meme \n **>>goodvidya**- Suggests a fun single-player game available on PC \n **>>goodanime**- Suggests a good japanese animated series")
	

client.run("MzQyMDQ3NDg5MzUzODQyNjg4.DGZaKQ.h8tgpwpdbS8ss7IhfiLi3DUlwwg")
