from aiogram.fsm.state import State, StatesGroup


class DialogStates(StatesGroup):
    chatting = State()


class AiDialogStates(StatesGroup):
    start = State()
