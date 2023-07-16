from aiogram.dispatcher.filters.state import State, StatesGroup

class Candidate(StatesGroup):
    waiting_for_new_man = State()
    waiting_for_unrewarded_man = State()