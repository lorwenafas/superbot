from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("ДМС💊")
      ],
      [
         KeyboardButton("Мессенджер Команда📱"),
         KeyboardButton ("Прочее👽")
      ],
      [
         KeyboardButton ("Чистота и порядок🔆")
      ],
      [
         KeyboardButton ("Реферальная программа👥"),
         KeyboardButton ("ВТБшки💰") 
      ],
      [
          KeyboardButton ("Как рассчитывается зарплата💵")
      ],
   ]
)

#ДМС

menu1 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("Скачать приложение")
      ],
      [
         KeyboardButton ("Узнать подробнее")
      ],
      [
         KeyboardButton ("3 месяца работаю, а ДМС не пришёл") 
      ],
   ]
)

#Рефералочка

menu2 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("Условия")
      ],
      [
         KeyboardButton ("Направить кандидата")
      ],
      [
         KeyboardButton ("Не пришло вознаграждение за кандидата") 
      ],
   ]
)

#ВТБешки

menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("За что можно получить ВТБшки?")
      ],
      [
         KeyboardButton ("Узнать баланс?")
      ],
      [
          KeyboardButton ("Как их потратить?")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

#Прочее

menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton ("Есть предложение, как сделать жизнь в КЦ лучше и интереснее?"),
         KeyboardButton ("Наши Telegram каналы"),
         KeyboardButton ("Такси")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

# МП Команда
menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("IOS"),
         KeyboardButton ("Andoid"),
         KeyboardButton ("Рабочий ПК"),
         KeyboardButton ("Техническая проблема")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

#Зарплата
menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("Оклад"),
         KeyboardButton ("Премия"),
         KeyboardButton ("Отпускные"),
         KeyboardButton ("Больничные")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

#Проблема РМ

menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton("Мебель"),
         KeyboardButton ("ИТ-оборудование"),
         KeyboardButton ("Холодно/жарко"),
         KeyboardButton("Другое")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

#Премия
menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton ("Расчёт премии"),
         KeyboardButton ("Расчёт доп. смен/овертаймов")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)

#Такси
menu3 = ReplyKeyboardMarkup(
   resize_keyboard=True, # default value - False
   one_time_keyboard=True, # default value - False
   keyboard=[
      [
         KeyboardButton ("Как правильно заказать"),
         KeyboardButton ("Возникли проблемы")
      ],
      [
         KeyboardButton ("<--Назад") 
      ]
   ]
)


# Назад

back = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
         [
            KeyboardButton("<--Назад")
         ]
    ]
)




"""
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("ДМС")
button2 = KeyboardButton("Мебель")
button3 = KeyboardButton("ИТ-оборудование")
button4 = KeyboardButton("Реферальная программа")
button5 = KeyboardButton("ВТБешки")
button6 = KeyboardButton("Прочее")
keyboard.add(button1, button2, button3, button4, button5, button6)
"""
