import discord
from discord.ext import commands
import yt_dlp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# YouTube downloader options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.tree.sync()

@bot.tree.command(name="convert", description="Convert YouTube video to MP3")
async def convert(interaction: discord.Interaction, url: str):
    await interaction.response.defer(thinking=True)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info['title']
            filename = f"{video_title}.mp3"

            # Download the audio
            ydl.download([url])

            # Check if file exists and its size
            if os.path.exists(filename) and os.path.getsize(filename) < 8 * 1024 * 1024:  # 8 MB limit
                await interaction.followup.send(f"Here's your MP3 for: {video_title}", file=discord.File(filename))
                os.remove(filename)  # Remove the file after sending
            else:
                await interaction.followup.send(f"The audio file for {video_title} is too large to send. Maximum file size is 8 MB.")
                if os.path.exists(filename):
                    os.remove(filename)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {str(e)}")
        if os.path.exists(filename):
            os.remove(filename)

@bot.tree.command(name="help", description="Show bot commands and usage")
async def help(interaction: discord.Interaction):
    help_text = """
    **YouTube to MP3 Converter Bot**

    Commands:
    `/convert <YouTube URL>` - Convert a YouTube video to MP3
    `/help` - Show this help message

    Usage:
    1. Use the `/convert` command followed by a valid YouTube URL.
    2. Wait for the bot to process and download the audio.
    3. The bot will send the MP3 file if it's under 8 MB.
    
    """
    await interaction.response.send_message(help_text)

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))