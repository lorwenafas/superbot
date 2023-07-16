from aiogram.dispatcher.filters.state import State, StatesGroup

class Clean(StatesGroup):
    waiting_for_cleaning_end = State()
    waiting_for_good = State()