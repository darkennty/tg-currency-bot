import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

BOT_TOKEN = os.getenv(
    'BOT_TOKEN',
    config.get('bot', 'token', fallback=None)
)
# BOT_TOKEN = config.get('bot', 'token', fallback=os.getenv('BOT_TOKEN'))
if not BOT_TOKEN:
    exit("Please provide BOT_TOKEN env variable")

PHOTO_YANDEX_DOG = 'https://cdn5.vedomosti.ru/image/2024/10/v2f2x/original-149g.jpg'
PHOTO_FROM_DISK = "C:\\Users\\victus\\OneDrive\\Pictures\\1200x0.jpg"
PHOTO_FROM_DISK_ID = "AgACAgIAAxkDAAOeZsDQEPK0Z3IBHIbaF7nPOn0cUlYAAgrmMRswdghK-Nrkerr12ZkBAAMCAANtAAM1BA"
PHOTO_CURRY = "https://cdn.britannica.com/11/261211-050-F39207C3/american-basketball-player-stephen-curry-celebrates-winning-the-olympic-gold-medal-on-the-podium-after-match-with-france-paris-olympics-2024.jpg"
PHOTO_CAT = 'https://toppng.com/uploads/preview/cat-png-transparent-cats-11563647803vsex8nq98w.png'
PHOTO_CAT_DISK = 'C:\\Users\\victus\\Desktop\\first-bot\\pngtree-isolated-cat-on-white-background-png-image_7094927.png'

def get_admin_ids():
    admin_ids = config.get('admin', 'admin_ids', fallback='')
    admin_ids = [admin_id.strip() for admin_id in admin_ids.split(',')]
    admin_ids = [
        int(admin_id)
        for admin_id in admin_ids
        if admin_id
    ]
    return admin_ids

BOT_ADMIN_USER_IDS = get_admin_ids()




