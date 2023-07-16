from aiogram.dispatcher.filters.state import State, StatesGroup

class Furniture(StatesGroup):
    waiting_for_information = State()