import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/fe60111b5bcbeffbb2b30.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm Amala!** \n\n"
  LUNA += "ð **I'm Working Properly** \n\n"
  LUNA += "ð **My Master : [á´á´É´É´á´](https://t.me/The_cat_lover0)** \n\n"
  LUNA += f"ð **Telethon Version : {tlhver}** \n\n"
  LUNA += f"ð **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan  ð**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/Amalarobot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/catmusicworld")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "â **bot berhasil di restart**\n\nâ¢ Admin list telah di **perbarui**"
  BUTTON = [[Button.url("á´á´á´á´á´á´s", "https://t.me/catmusicworld")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
