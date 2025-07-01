{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import time\
import telebot\
from bs4 import BeautifulSoup\
\
# === CONFIGURATION ===\
BOT_TOKEN = "TON_TOKEN_ICI"  # Remplace par ton token Telegram Bot\
CHAT_ID = "TON_CHAT_ID_ICI"  # Remplace par ton chat ID Telegram\
\
# Ton URL de recherche Vinted\
SEARCH_URL = "https://www.vinted.com/catalog?time=1751381716&catalog_from=0&size_ids[]=208&brand_ids[]=395367&page=1&status_ids[]=6&status_ids[]=1&status_ids[]=2&price_from=1.5&currency=USD&price_to=25"\
\
bot = telebot.TeleBot(BOT_TOKEN)\
seen_items = set()\
\
def check_vinted():\
    headers = \{\
        "User-Agent": "Mozilla/5.0"\
    \}\
    response = requests.get(SEARCH_URL, headers=headers)\
    soup = BeautifulSoup(response.text, "html.parser")\
    items = soup.find_all("a", href=True)\
\
    for item in items:\
        href = item['href']\
        if "/items/" in href and href not in seen_items:\
            seen_items.add(href)\
            full_url = "https://www.vinted.com" + href\
            print("Nouvelle annonce :", full_url)\
            bot.send_message(CHAT_ID, f"
\f1 \uc0\u55357 \u56596 
\f0  Nouvelle annonce rep\'e9r\'e9e : \{full_url\}")\
\
# Boucle toutes les 60 sec\
while True:\
    try:\
        check_vinted()\
    except Exception as e:\
        print("Erreur :", e)\
    time.sleep(60)\
}