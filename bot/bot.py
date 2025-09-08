import time
import telepot
from telepot.loop import MessageLoop
from telegram.ext import *
from Whisper import load_model_whisper, get_lyrics
import requests


API_TOKEN = "IAmNotGoingToLeakMyToken:)"
audio_file_path = 'audio.mp3'
MODEL_SIZE = 'large'


def download_mp3(audio_info):
    file_id = audio_info['file_id']
    # Get the file path using the file_id
    file_info = bot.getFile(file_id)
    file_path = file_info['file_path']
    
    # Construct the URL to download the file
    download_url = f'https://api.telegram.org/file/bot{API_TOKEN}/{file_path}'
    
    # Download the audio file
    response = requests.get(download_url)
    # Save the audio file as MP3
    with open(audio_file_path, 'wb') as f:
        f.write(response.content)
    
    print('Mp3 has been downloaded...')

def handle(msg):
    """
    A function that will be invoked when a message is recevied by the bot.
    """
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "audio":
        audio_info = msg['audio']
        download_mp3(audio_info)
        reply = get_lyrics(model, audio_file_path)
        print(reply)
        bot.sendMessage(chat_id, reply)

if __name__ == "__main__":
    # Provide your bot's token
    bot = telepot.Bot(API_TOKEN)
    print("Bot starting...")
    model = load_model_whisper()
    print("Bot started.")
    MessageLoop(bot, handle).run_as_thread()
    while True:
        time.sleep(10)