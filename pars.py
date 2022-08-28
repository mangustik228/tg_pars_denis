from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetFullChannelRequest
import os, time, json
from dotenv import load_dotenv

dotenv_path = os.path.join('dot.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

SEND_TO_CHANNEL = os.environ['SEND_TO_CHANNEL']
CHANNEL = os.environ['CHANNEL_URL']
SESSION_NAME = os.environ['TELEGRAM_SESSION_NAME']
API_HASH = os.environ['TELEGRAM_API_HASH']
API_ID = os.environ['TELEGRAM_API_ID']
CURRENT_PHOTO = 0
CURRENT_TITLE = '' 

def main(channel, session_name, api_hash, api_id):
    ''' 
    '''
    with TelegramClient(session_name, api_id, api_hash) as client:
        # да, да... храню текующие id и название в глобальной переменной
        global CURRENT_PHOTO, CURRENT_TITLE
        ch = client.get_entity(channel) 
        ch_full = client(GetFullChannelRequest(channel=ch))
        info = json.loads(ch_full.to_json())
        photo_id = info.get('chats')[0].get('photo').get('photo_id')
        channel_name = info.get('chats')[0].get('title')
        
        if photo_id != CURRENT_PHOTO or channel_name != CURRENT_TITLE:
            photo = client.download_profile_photo(channel)
            client.send_file(
                SEND_TO_CHANNEL,
                photo, 
                caption=str(channel_name))
            CURRENT_PHOTO = photo_id
            CURRENT_TITLE = channel_name
        # else:
        #     print('Опять ничего не обновилось')
       
if __name__ == '__main__':
    while True:
        main(CHANNEL, SESSION_NAME, API_HASH, API_ID)
        time.sleep(30)