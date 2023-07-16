from aiogram.dispatcher.filters.state import State, StatesGroup

class comanda(StatesGroup):
    waiting_for_comanda = State()
