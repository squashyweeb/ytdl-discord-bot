# Discord Video Downloader Bot

This Discord bot allows you to download videos from links provided in Discord messages using `yt-dlp`. The bot saves videos with a timestamp in the filename to avoid overwriting existing files.

## Features

- **Download Videos**: Processes video links and downloads them using `yt-dlp`.
- **Progress Updates**: Provides real-time download progress in the Discord channel.
- **Timestamped Filenames**: Saves videos with a timestamp in the filename to ensure uniqueness.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `yt-dlp` (YouTube-DL fork)
- A Discord bot token

## Installation

1. **Clone the Repository**
   
   git clone https://github.com/yourusername/discord-video-downloader-bot.git
   cd discord-video-downloader-bot

2. **Install Dependencies**

   Install the required Python packages:

   pip install -r requirements.txt

   Create a `requirements.txt` file with the following content:

   discord.py

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory with the following content:

   DISCORD_TOKEN=your_discord_bot_token

   Replace `your_discord_bot_token` with your actual Discord bot token.

4. **Create the `run.py` File**

   Save the provided script as `run.py` in your project directory.

## Usage

1. **Run the Bot**

   Start the bot with:

   python run.py

2. **Interact with the Bot**

   - Send a message in any channel with the format `/videolink: <video_link>`.
   - The bot will send a message indicating that it is processing the video link and will update with the download progress.

## Code Explanation

- **Imports and Setup**: The bot uses `discord.py` and `subprocess` to handle Discord interactions and video downloads.
- **Event Handling**: `on_ready` confirms the bot is running. `on_message` listens for messages starting with `/videolink:` and processes the video link.
- **Video Downloading**: `send_download_message` sends an initial message and calls `run_yt_dlp` to download the video. `run_yt_dlp` runs `yt-dlp` in a subprocess and updates the progress in the message.

## Troubleshooting

- **Token Not Found**: Ensure `DISCORD_TOKEN` is correctly set in the `.env` file.
- **Download Failures**: Check that `yt-dlp` is installed and accessible.

## Contributing

Feel free to open issues or submit pull requests with improvements or suggestions!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
