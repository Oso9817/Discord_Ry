import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from weatherBot import *
from ritoBot import *
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''	
bot = commands.Bot(command_prefix='!', description=description)	
@bot.command(pass_context = True)
async def weather(ctx, state, *, city):
		try:
			await bot.say(weatherGet(state, city.replace(' ', '%20')).current_temp)
			print('test')
		except Exception as msg:
			await bot.say('OwO! We made a fucky wucky!')
			print('Could not pull weatherGet({0}, {1}).current_temp. {2}'.format(state, city, msg))	
@bot.command()
async def ryan():
		await bot.say('Homies dick 12 inches long soft god damn')		
@bot.command(pass_context = True)
async def ally(ctx, *, champEntry):
				
		try:
			await bot.say((discord_rito(champEntry).allyTips1))
			print('await bot.say((discord_rito({0}).allyTips1))'.format(champEntry))
		except Exception as e:
			await bot.say("Couldn't get tips")
			raise e				
@bot.command(pass_context = True)
async def champ(ctx, *, champEntry):
		try:
			await bot.say((discord_rito(champEntry).skillKit))
			print('await bot.say((discord_rito({0}).skillKit))'.format(champEntry))
		except Exception as e:
			await bot.say("Couldn't get spells")
			raise e	
bot.run('')