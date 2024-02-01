from aiogram.fsm.state import State, StatesGroup

class Quiz(StatesGroup):
    translation = State()
    correct = State()
    incorrect = State()