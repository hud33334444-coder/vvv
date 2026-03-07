from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

SAMPLE = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="SAMPLE", callback_data="SAMPLE")]]
)


def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💬 Начать диалог"),
                KeyboardButton(text="⏹️ Закончить диалог"),
            ],
            [KeyboardButton(text="🆘 Поддержка"), KeyboardButton(text="👤 Профиль")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
