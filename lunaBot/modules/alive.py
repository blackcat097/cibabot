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
  LUNA += "💎 **I'm Working Properly** \n\n"
  LUNA += "💎 **My Master : [ᴋᴀɴɴᴀ](https://t.me/The_cat_lover0)** \n\n"
  LUNA += f"💎 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"💎 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan  💚**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Amalarobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/catmusicworld")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **bot berhasil di restart**\n\n• Admin list telah di **perbarui**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/catmusicworld")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
