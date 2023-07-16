# ДМС
@dp.message_handler(text=["ДМС💊"])
def button(message):
   

   menu = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("ДМС💊")
      ],
      [
         KeyboardButton ("Мебель🪑"),
         KeyboardButton ("ИТ-оборудование🖥️")
      ],
      [
         KeyboardButton ("Реферальная программа👥"),
         KeyboardButton ("ВТБешки💰"),
         KeyboardButton ("Прочее")
         
      ],
   ]
)