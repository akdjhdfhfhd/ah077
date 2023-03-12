from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت لمجموعتڪ ✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامر ⚕️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="☆ الاعدادات ☆", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت لمجموعتڪ ✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامر ⚕️", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="مطور البوت 👨‍💻", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة البوت ⚙️", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
