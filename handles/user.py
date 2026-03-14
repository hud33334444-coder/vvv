import re

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from database.db import session
from utils.rqs import send_request
from utils.states import DialogStates
from utils.keyboard import get_main_keyboard
from database.repo import UserRepository

user = Router()


@user.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать! Выберите действие:", reply_markup=get_main_keyboard()
    )


@user.message(F.text == "🆘 Поддержка")
async def help(message: Message):
    await message.answer("📞 Поддержка", reply_markup=get_main_keyboard())


@user.message(F.text == "💬 Начать диалог")
async def test(message: Message, state: FSMContext):
    await state.set_state(DialogStates.chatting)
    await message.answer(
        "Диалог начат! Напишите сообщение (кроме кнопок).",
        reply_markup=get_main_keyboard(),
    )
    await state.set_state(DialogStates.chatting)


@user.message(F.text == "⏹️ Закончить диалог")
async def end_dialog(message: Message, state: FSMContext):
    await message.answer("Диалог завершен", reply_markup=get_main_keyboard())
    await state.clear()


@user.message(DialogStates.chatting)
async def dialog(message: Message):
    response = await send_request(message.text)
    await message.answer(response)


@user.message(F.text == "👤 Профиль")
async def profile_handler(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "нету юзера"
    await message.answer(
        f"ID: `{user_id}`\n" f"Username: @{username}\n",
        parse_mode="Markdown",
        reply_markup=get_main_keyboard(),
    )


@user.message(F.text == "update")
async def create_user(message: Message):
    re = UserRepository(session())
    await re.update(tid=message.from_user.id, username="changed")
    await re.close()
    await message.answer("Обновили")


@user.message(F.text == "delete")
async def delete_user(message: Message):
    rep = UserRepository(session())
    await rep.delete(tid=message.from_user.id)
    await rep.close()
    await message.answer("Удалили")
