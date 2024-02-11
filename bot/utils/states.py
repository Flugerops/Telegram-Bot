from aiogram.fsm.state import State, StatesGroup

class Quiz(StatesGroup):
    game = State()
    check_mod = State()
    correct = State()
    incorrect = State()
    
class Translate(StatesGroup):
    message_check = State()
    translation = State()