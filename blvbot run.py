# bot.py
import os
import schedule
import datetime
import time
from datetime import datetime
from datetime import date
import asyncio
import threading
import discord
import schedule
from discord.ext import commands, tasks

import runpy
import datetime
from datetime import date
import schedule

simRan = False

        



TOKEN = 'OTcyMDU2MzgzMzg0MDg0NTEw.G5myQ6.YOjwOoL1rLjqAowGmAaDsTioXo9OLJyODld-yA'


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


chan1 =1172023374004895866
chan2 =1172023338797891725 
chan3 =1172023274151088158
chan4 =1172023217003708509
chan5 =1172023147617325056
chan6 =909543275482992662

testChan = 1021615035698655302

@tasks.loop(hours=24)
async def called_once_a_day():
    
    #testing
    #message_channel = client.get_channel(1021615035698655302)
    #predictions
    message_channel = client.get_channel(testChan)
    
    
    print(f"Got channel {message_channel}")
    
    
    dt = date.today() + datetime.timedelta(days = 6)
    
    
  
    wkday = dt.strftime("%a")
    day = dt.strftime("%d")
    mo = dt.strftime("%m")
    
    wee = wkday + ' ' + dt.strftime("%x")
    
    await message_channel.send("""\n-------------------------------------------------------------------------------------\n
running sim, \n """ + '**'+wee+'**' +" at **10am** \n **payload mass: 3700g** \n gimme 20 seconds...") 
    runpy.run_path('webScrapetest6.py')
    
    with open("Output.txt", "r") as text_file:
        linky = text_file.read()
        text_file.close()
    
    await message_channel.send(linky, file=discord.File('currSim.png'))
    
    

@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")



@client.event
async def on_ready():
    print('this life is a lie!')
    print('-------------------------')
    #await channel.send('i am here')
    #checkTime()

@client.command()
async def intro(ctx):
    await ctx.send(''' My purpose is to run sims 6 days out at 8:30pm every day, and link you to the site if you wanna change times around. 
More functionality coming soon. Existence is pain.''')
    #await ctx.send('here da sim', file=discord.File('currSim.png'))
    
@client.command()
async def goodbye(ctx):
    await ctx.send('cya')

@client.command()
async def sim(ctx):
    # dt = date.today() + datetime.timedelta(days = 6)
    
    # wee = dt.strftime("%x")
    # wkday = dt.strftime("%a")
    # day = dt.strftime("%d")
    # mo = dt.strftime("%m")
    
    # await ctx.send("running sim at maximum distance out, " + '**'+wee+'**' +" **at 10am** \n payload mass 3700 \n gimme 20 seconds...") 
    # runpy.run_path('webScrapetest.py')
    # await ctx.send('', file=discord.File('currSim.png'))
    await called_once_a_day()

called_once_a_day.start()

client.run(TOKEN)