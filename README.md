# Discord YouTube to MP3 Bot

This Discord bot allows users to convert YouTube videos to MP3 files using simple slash commands.

## Features

- Convert YouTube videos to MP3 format
- Easy-to-use slash commands
- Automatic file cleanup after sending

## Prerequisites

- Python 3.8 or higher
- ffmpeg installed on your system
- Discord Bot Token

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/troycallen/disc-yt2mp3.git
   cd disc-yt2mp3
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token
   ```
   Replace `your_discord_bot_token` with your actual Discord bot token.

## Usage

Run the bot:
```
python main.py
```

## Commands

- `/convert <YouTube URL>`: Convert a YouTube video to MP3 and send the file
- `/help`: Display help information about the bot's commands

## Limitations

- Due to Discord's file size limitations, the bot can only send MP3 files up to 8 MB in size.

## License

[MIT]