import os
import discord
from discord.ext import commands
import subprocess
import datetime

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No token found. Please set the DISCORD_TOKEN environment variable.")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/videolink:'):
        link = message.content.split(' ')[1]
        print(f'Processing video link: {link}')
        await send_download_message(message.channel, link)

async def send_download_message(channel, link):
    msg = await channel.send(f'Processing video link: {link}\nStarting download...')
    file_path = await run_yt_dlp(link, msg)
    
    if file_path:
        await msg.edit(content=f'Video downloaded successfully: {file_path}')
    else:
        await msg.edit(content='Failed to download the video.')

async def run_yt_dlp(link, msg):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f'/mnt/external_drive/video_{current_date}.mp4'

    try:
        process = subprocess.Popen(
            ['yt-dlp', link, '--output', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        for line in process.stdout:
            if '[download]' in line and '%' in line:
                progress = line.split('%')[0].strip().split()[-1]
                await msg.edit(content=f'Downloading... {progress}%')

        process.wait()
        
        if process.returncode == 0:
            return file_path
        else:
            return None
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')
        return None

client.run(TOKEN)
