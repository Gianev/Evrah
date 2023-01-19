import discord
import random
import requests
import json
from weather import *
from mapselect import *
from PIL import Image, ImageChops, ImageDraw, ImageFont

TOKEN = 'OTIyMjAzNzg4ODAxMTE0MTQy.Yb-DNA.lvm44kNuCFH5v6AvCj0HTAQYz5s'
api_key = '40649322cac2c18aa7c9075b48a7e35a'
client = discord.Client()

@client.event
async  def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    await on_message.channel.send(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    await on_message.channel.send(f'{member} has left the server :(')

@client.event
async  def on_message(message):
    username = str(message.author).split('#')[0]
    user_message= str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == '!insult':
        await message.channel.send('HI BOZO')

    if user_message.lower() == '!bbw':
        await message.channel.send('Ferdinand loves ')

    if user_message.lower() == '!random':
        number = random.randrange(10000)
        await message.channel.send('Your random number is ' + str(number))

    if user_message.lower() == '!flip':
        face = ''
        rando = random.randrange(2)
        if rando == 0:
            face = 'tails'
        else:
            face = 'heads'
        await message.channel.send(face)

    if user_message.lower() == '!map':
        num = random.randrange(7)

        await message.channel.send(embed =final_message_maps(pick(num)))



    if user_message.lower() == '!help':
        await message.channel.send('Use !random for a random number')
        await message.channel.send('Use !flip to flip a coin')
        await message.channel.send('Use sus.[name] to call someone sus')

    if message.content.startswith('sus.'):
        name = message.content.replace('sus.', '')
        await message.channel.send(file = discord.File('sus.jpg'))
        await message.channel.send('you are sus '+ name)

    if message.author != client.user and message.content.startswith('w.'):
        if len(message.content.replace('w.', '')) >= 1:
            location = message.content.replace('w.', '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))

client.run(TOKEN)