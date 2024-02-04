from aiogram.fsm.state import State, StatesGroup

class Quiz(StatesGroup):
    translation = State()
    check_mod = State()
    correct = State()
    incorrect = State()