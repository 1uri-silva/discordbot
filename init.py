import json
import requests
import discord
from random import random
import asyncio
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

def fetch_data():
  x = input('Enter your url here: ')
  res = requests.get(x)
  return json.loads(res.text)
    
def write_archive():
  response = fetch_data()
  name_file = random().__floor__()
  with open(str(name_file) + '.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=2)
  return str(name_file) + '.json'

async def timer():
  await client.wait_until_ready()
  channel = client.get_channel(int(config.get('TESTSERVER')))
  
  while True:
    file = write_archive()
    await channel.send('@everyone', file=discord.File(file))
    await asyncio.sleep(float(config.get('TIMESC'))) #seconds
    
    if os.path.exists(file):
      os.remove(file)
    else:
      print("The file does not exist")
      
client = discord.Client()

@client.event
async def on_ready():
  print('Estou online')
  await timer()

client.run(config.get('TOKEN'))
    