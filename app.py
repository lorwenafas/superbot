from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import logging

from keyboards import menu, menu1, menu2, menu3, back
from states import Furniture, Candidate, Clean, comanda


API_TOKEN = "6220809223:AAGIUlYSj86lwwY_I3H8tkkrY2S3Rz37crk" #"6190703718:AAGLJgg90Xj8-V4Fik9vGWP9eyLKT73XXrc"
ADMINS = [556370377] # список telegram id администраторов

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
   await message.reply("Привет, коллега! Что умеет этот бот? Если у тебя что-то сломалось, хочешь узнать подробнее о ДМС, реферальной программе или ВТБешках, то выбери корректную тематику и следуй дальнейшей инструкции. Хорошего тебе дня😎", reply_markup=menu,)


# ДМС
@dp.message_handler(text=["ДМС💊"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Скачать приложение")
    keyboard.add(button_1)
    button_2 = "Узнать подробнее"
    keyboard.add(button_2)
    button_3 = "3 месяца работаю, а ДМС не пришёл"
    keyboard.add(button_3)
    button_4 = "<--Назад"
    keyboard.add(button_4)
    await message.answer("Какой у тебя вопрос?", reply_markup=keyboard)

@dp.message_handler(text=["Скачать приложение"])
async def echo(message: types.Message):
   await message.answer('<a href="https://apps.apple.com/ru/app/%D1%81%D0%BE%D0%B3%D0%B0%D0%B7-%D0%BC%D0%B5%D0%B4-%D0%BF%D0%BE%D0%BB%D0%B8%D1%81-%D0%BE%D0%BC%D1%81-%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D0%B0/id1583604507">Для IOS.</a>',parse_mode="HTML")
   await message.answer('<a href="https://play.google.com/store/apps/details?id=ru.sogaz.app&hl=ru">Для Android.</a>',parse_mode="HTML" , reply_markup=menu)

@dp.message_handler(text=["Узнать подробнее"])
async def echo(message: types.Message):
   await message.answer ("Если хочешь узнать подробнее об услугах и медицинских организациях, которые входят в твой ДМС, обратись на ГЛ Согаза 8(800)333 44 19.", reply_markup=menu)

@dp.message_handler(text=["3 месяца работаю, а ДМС не пришёл"])
async def echo(message: types.Message):
   await message.answer ("ДМС приходит на рабочую почту в течение 2-х недель с даты окончания испытательного срока. Если срок вышел, а твой ДМС так и не пришёл, то напиши на почту DMS_GO@sogaz.ru или обратись на ГЛ Согаза 8(800)333 44 19.", reply_markup=menu)
  
@dp.message_handler(text=["<--Назад"])
async def echo(message: types.Message):
   await message.answer ("Хорошего дня☺️", reply_markup=menu)

# МП Команда
@dp.message_handler(text=["Мессенджер Команда📱"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="IOS")
    keyboard.add(button_1)
    button_2 = "Andoid"
    keyboard.add(button_2)
    button_3 = "Рабочий ПК"
    keyboard.add(button_3)
    button_4 = "Техническая проблема"
    keyboard.add(button_4)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("На каком устройстве необходимо выполнить вход?", reply_markup=keyboard)

@dp.message_handler(text=["IOS"])
async def echo(message: types.Message):
   await message.answer ('<a href="https://apps.apple.com/ru/app/%D0%BC%D0%B5%D1%81%D1%81%D0%B5%D0%BD%D0%B4%D0%B6%D0%B5%D1%80-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0/id1616562120">Скачай приложение для IOS. Обрати внимание, что для входа нужно ввести рабочую почту. Затем ввести код, который придёт в Outlook.</a>',parse_mode="HTML", reply_markup=menu)

@dp.message_handler(text=["Andoid"])
async def echo(message: types.Message):
   await message.answer ('<a href="https://play.google.com/store/apps/details?id=center.basis.MessengerTeam">Скачай приложение для Android. Обрати внимание, что для входа нужно ввести рабочую почту. Затем ввести код, который придёт в Outlook.</a>',parse_mode="HTML", reply_markup=menu)

@dp.message_handler(text=["Рабочий ПК"])
async def echo(message: types.Message):
   await message.answer ("Для того, чтобы зайти в Команду с ПК, нужно пройти регистрацию в МП с твоего телефона. После того, как ты установил приложение на телефон и выполнил на нём вход, открой команду на ПК (на рабочем столе есть иконка), затем зайди в приложении на телефоне в Настройки--> Мессенджер команда Web и отсканируй QR-код с монитора компьютера.", reply_markup=menu)

@dp.message_handler(text=["Техническая проблема"])
async def echo(message: types.Message):
   user_full_name = message.from_user.full_name
   await message.answer ("Укажи ФИО, номер рабочего места и подробно опиши ситуацию:", reply_markup=back)
   await comanda.waiting_for_comanda.set()

@dp.message_handler(state=comanda.waiting_for_comanda, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Тех проблеиа с МП Команда. Передай инф-ию Дыневой Айжан. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течение 3-х рабочих дней.", reply_markup=menu)
      await state.finish()


@dp.message_handler(text=["<--Назад"])
async def echo(message: types.Message):
   await message.answer ("Хорошего дня☺️", reply_markup=menu)

# Проблема РМ
@dp.message_handler(text=["Чистота и порядок🔆"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Мебель")
    keyboard.add(button_1)
    button_2 = "ИТ-оборудование"
    keyboard.add(button_2)
    button_3 = "Холодно/жарко"
    keyboard.add(button_3)
    button_4 = "Другое"
    keyboard.add(button_4)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("Что именно случилось?", reply_markup=keyboard)

@dp.message_handler(text=["Мебель"])
async def echo(message: types.Message):
   await message.answer ("Укажи ФИО, номер рабочего места и подробно опиши ситуацию:", reply_markup=back)
   await Furniture.waiting_for_information.set()

@dp.message_handler(state=Furniture.waiting_for_information, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Сломана мебель. Нужно завести заявку. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течение 3-х рабочих дней.", reply_markup=menu)
      await state.finish()

@dp.message_handler(text=["ИТ-оборудование"])
async def echo(message: types.Message):
   await message.answer ("Укажи ФИО, номер рабочего места и подробно опиши ситуацию:", reply_markup=back)
   await Furniture.waiting_for_information.set()

@dp.message_handler(state=Furniture.waiting_for_information, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Сломано ИТ-оборудование. Нужно завести заявку. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течение 3-х рабочих дней.", reply_markup=menu)
      await state.finish()      

@dp.message_handler(text=["Холодно/жарко"])
async def echo(message: types.Message):
   await message.answer ("Укажи ФИО, номер рабочего места и подробно опиши ситуацию:", reply_markup=back)
   await Furniture.waiting_for_information.set()

@dp.message_handler(state=Furniture.waiting_for_information, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Проблемы с кондиционером. Нужно завести заявку. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течение 3-х рабочих дней.", reply_markup=menu)
      await state.finish()   

@dp.message_handler(text=["Другое"])
async def echo(message: types.Message):
   await message.answer ("Опиши подробно ситуацию. Если что-то разлил или сильно испачкал, не переживай! Со всеми бывают неловкие ситуации. Укажи номер рабочего места и комментарий, чтобы служба клининга могла это исправить. Если в туалете нет туалетной бумаги, мыла, тоже опиши ситуацию. Если что-то ещё необходимо убрать или исправить - сообщи.", reply_markup=back)
   await Clean.waiting_for_cleaning_end.set()

@dp.message_handler(state=Clean.waiting_for_cleaning_end, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Необходимо сделать заявку на клининг. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос передан администратору", reply_markup=menu)
      await state.finish()         


# Реферальная программа
@dp.message_handler(text=["Реферальная программа👥"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Условия")
    keyboard.add(button_1)
    button_2 = "Направить кандидата"
    keyboard.add(button_2)
    button_3 = "Не пришло вознаграждение за кандидата"
    keyboard.add(button_3)
    button_4 = "<--Назад"
    keyboard.add(button_4)
    await message.answer("Какой у тебя вопрос?", reply_markup=keyboard)

@dp.message_handler(text=["Условия"])
async def echo(message: types.Message):
   await message.answer("Когда приведенный тобой сотрудник успешно пройдет обучение и испытательный срок 3 месяца, и будет трудоустроен, ты получишь бонус - 10 тысяч рублей (10 тыс. руб. ты получаешь за каждого приведенного сотрудника). Подробнее: prohorovao@vtb.ru", reply_markup=menu)

@dp.message_handler(text=["Направить кандидата"])
async def echo(message: types.Message):
   await message.answer ("Укажи ФИО, ДР и контактный номер телефона.", reply_markup=back)
   await Candidate.waiting_for_new_man.set()

@dp.message_handler(state=Candidate.waiting_for_new_man, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Новый кандидат. Передай инф-ию Прохоровой Ольге. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течении 3-х рабочих дней.", reply_markup=menu)
      await state.finish()

@dp.message_handler(text=["Не пришло вознаграждение за кандидата"])
async def echo(message: types.Message):
    await message.answer ("Укажи ФИО кандидата, за которого не пришло вознаграждение.", reply_markup=back)
    await Candidate.waiting_for_unrewarded_man.set()
   
@dp.message_handler(state=Candidate.waiting_for_unrewarded_man, content_types=types.ContentType.TEXT)
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Не получено вознаграждение за кандидата. Передай инф-ию Прохоровой Ольге. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос в работе. Информацию можешь получить у своего РГ в течении 3-х рабочих дней.", reply_markup=menu)
      await state.finish()

   #ВТБешки
@dp.message_handler(text=["ВТБшки💰"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="За что можно получить ВТБшки?")
    keyboard.add(button_1)
    button_2 = "Узнать баланс?"
    keyboard.add(button_2)
    button_3 = "Как их потратить?"
    keyboard.add(button_3)
    button_4 = "<--Назад"
    keyboard.add(button_4)
    await message.answer("Какой у тебя вопрос?", reply_markup=keyboard)

@dp.message_handler(text=["За что можно получить ВТБшки?"])
async def echo(message: types.Message):
   await message.answer("1.За лучшие показатели месяца. 2.Лидеры внутрифункционального рейтинга. 3.Бонус от директора (лидеры доп.смен, овертаймов, ночных смен и лучшие ФТ/НСТ) 4.Активное участие в конкурсах и викторинах КЦ.",reply_markup=menu)

@dp.message_handler(text=["Узнать баланс?"])
async def echo(message: types.Message):
   await message.answer ("Не знаешь где посмотреть баланс? Личный кабинет ВТБ pro --> выбирай КЦ. Если личный кабинет недоступен, можешь написать на п/я Голос ДКО", reply_markup=menu)

@dp.message_handler(text=["Как их потратить?"])
async def echo(message: types.Message):
   await message.answer ("Посмотреть и приобрести товар можно в группе Вконтакте https://vk.com/dko_vtb.", reply_markup=menu)
  
@dp.message_handler(text=["<--Назад"])
async def echo(message: types.Message):
   await message.answer ("Хорошего дня☺️", reply_markup=menu)

#Прочее
@dp.message_handler(text=["Прочее👽"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Есть предложение, как сделать жизнь в КЦ лучше и интереснее?")
    keyboard.add(button_1)   
    button_3 = "Наши Telegram каналы"
    keyboard.add(button_3)
    button_4 = "Такси"
    keyboard.add(button_4)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("Какой у тебя вопрос?", reply_markup=keyboard)


@dp.message_handler(text=["Есть предложение, как сделать жизнь в КЦ лучше и интереснее?"])
async def echo(message: types.Message):
   await message.answer ("Опиши подробно свою идею и укажи номер группы🤩", reply_markup=back)
   await Clean.waiting_for_good.set()

@dp.message_handler(state=Clean.waiting_for_good, content_types=types.ContentType.ANY) # поменять текст!
async def echo(message: types.Message, state: FSMContext):
   if message.text == "<--Назад":
      await message.answer ("Хорошего дня☺️", reply_markup=menu)
      await state.finish()
   else:
      text_for_admin = "Новое предложение. Передай инф-ию Русяевой Анне. Текст заявки:\n" + message.text
      for id in ADMINS:
         await bot.send_message(id, text_for_admin)
      await message.answer("Спасибо! Запрос передан администратору", reply_markup=menu)
      await state.finish()

@dp.message_handler(text=["Наши Telegram каналы"])
async def echo(message: types.Message):
   await message.answer('<a href="https://t.me/+rgq0RVPE-dwxMWQ6">Карьера ВТБ.</a>',parse_mode="HTML")
   await message.answer('<a href="https://t.me/+Fn2KGIQd05RjMjFi">КОСМО.NEWS.</a>',parse_mode="HTML")
   await message.answer('<a href="https://t.me/joinchat/c9A-SXMvCw9lYzY6">ДКО ВТБ.</a>',parse_mode="HTML" , reply_markup=menu)

@dp.message_handler(text=["Такси"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Как правильно заказать")
    keyboard.add(button_1)
    button_2 = "Возникли проблемы"
    keyboard.add(button_2)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("Уточни вопрос.", reply_markup=keyboard)

@dp.message_handler(text=["Как правильно заказать"])
async def echo(message: types.Message):
   await message.answer ("В будний день передай инф-ию о необходимости заказа такси своему РГ. Если ты работаешь в субботу или в воскресенье, направь инф-ию дежурному РГ ответным письмом на его запрос направить такси в Outlook. Обрати внимание, что данная информация должна быть направлена до 17:00 и строго по форме, указанной в письме.", reply_markup=menu)

@dp.message_handler(text=["Возникли проблемы"])
async def echo(message: types.Message):
   await message.answer ("Если такси не приехало или водитель отказался выполнять заказ, позвони ДРГ по номеру телефона, который он указал в приветсвенном письме в почте. Если ДРГ недоступен, то вызови такси самостоятельно и передай эту инф-ию своему РГ, чтобы мы могли тебе компенсировать эти затраты.", reply_markup=menu)

   #Зарплата
@dp.message_handler(text=["Как рассчитывается зарплата💵"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Оклад")
    keyboard.add(button_1)
    button_2 = "Премия"
    keyboard.add(button_2)
    button_3 = "Отпускные"
    keyboard.add(button_3)
    button_4 = "Больничные"
    keyboard.add(button_4)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("Какой вид выплат тебя интересует?", reply_markup=keyboard)

@dp.message_handler(text=["Оклад"])
async def echo(message: types.Message):
   await message.answer ("Оклад работникам выплачивается 2 раза в месяц: 15 и 30 числа. Выплата может быть произведена раньше, если 15 или 30 число выпадает на выходной день (сб/вс). Оклад рассчитывается исходя из количества отработанных часов в месяце (мы работаем на СУРВ),умноженного на стоимость часа. СУРВ - это суммированный учёт рабочего времени. Стоимость часа разная, в зависимости от квартала, так как разное количество рабочих часов по производственному календарю. Для расчета стоимости часа необходимо: тройной оклад/количество часов в квартале. Например: оклад работника 30 000 руб., 3 кв. 2023 - 520 часов. Расчёт оклада в 3 кв 2023: cтоимость часа в 3 кв. 2023 = (30 000*3)/520 = 173.08 руб. Июль 2023 = 173.08 * 168 (рабочих часов) = 29 076 руб. Август 2023 = 173.08 * 184 часа = 31 847 руб. Сентябрь 2023 = 173.08 * 168 (рабочих часов) = 29 076 руб. Как мы видим, в июле и сентябре оклад на 924 руб. меньше среднего оклада по кварталу. При этом в августе на 1 847 руб. выше среднего по кварталу. Проще говоря, сколько отработал, столько и получил. Чем меньше на больничном, тем больше гарантированный оклад, и как следствие, выше премия😉", reply_markup=menu)

@dp.message_handler(text=["Премия"])
async def echo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Расчёт премии")
    keyboard.add(button_1)
    button_2 = "Расчёт доп. смен/овертаймов"
    keyboard.add(button_2)
    button_5 = "<--Назад"
    keyboard.add(button_5)
    await message.answer("Уточни вопрос.", reply_markup=keyboard)
     
@dp.message_handler(text=["Расчёт премии"])
async def echo(message: types.Message):
   await message.answer ("Премия считается по формуле: (оклад * % премии (зависит от направления)) * ИПП.", reply_markup=menu)
   await message.answer ("ИПП считается: ((35% * на коэффициент АНТ)+(35% * на коэффициент по продажам)+(30% * на коэффициент по ДН))* коэффициент НКОК.", reply_markup=menu)

@dp.message_handler(text=["Расчёт доп. смен/овертаймов"])
async def echo(message: types.Message):
   await message.answer ("Доп. смена считается так: 32000 * 3 (кол-во мес. в квартале) = 96000. В 3 квартале 2023 - 520 часов. 96000/520= 184,60 - стоимость 1 часа. В доп. смене 184,6 * 2 = 369,23 рублей. Если ты вышел, предположим, на 9 часов, то получишь 369,23 * 9 = 3323 рубля.", reply_markup=menu)
   await message.answer ("Овертайм - время, когда ты по просьбе своего руководителя задерживаешься в линии после работы или выходишь на прием звонков до начала смены. Часы, отработанные в овертайм выплачиваются в конце квартала. Первые два часа овертайма в квартале рассчитываются по ставке - 1,5. Далее все овертаймы идут по двойной оплате.", reply_markup=menu)

@dp.message_handler(text=["Отпускные"])
async def echo(message: types.Message):
   await message.answer ("В 2023 году общая формула, по которой следует считать отпускные, установлена на законодательном уровне. Выглядит формула следующим образом: Отпускные= Среднедневной заработок х Количество дней отпуска. Количество дней отпуска – это число календарных дней в период отпуска за минусом праздничных дней. Праздничные дни в отпуск не входят и не оплачиваются.", reply_markup=menu)

@dp.message_handler(text=["Больничные"])
async def echo(message: types.Message):
   await message.answer ("Ве­ли­чи­на по­со­бия (П), на­чис­ля­е­мо­го ра­бот­ни­ку за пе­ри­од вре­мен­ной нетру­до­спо­соб­но­сти, опре­де­ля­ет­ся по сле­ду­ю­щей фор­му­ле: П = СДЗ х С% х Д, где СДЗ – сред­ний днев­ной за­ра­бо­ток; С% — про­цент, за­ви­ся­щий от стра­хо­во­го стажа ра­бот­ни­ка (при стаже больше 8 лет работник получает 100% от среднего заработка, от 5 до 8 лет — 80%, меньше 5 лет — 60%); Д – ко­ли­че­ство дней нетру­до­спо­соб­но­сти. Сред­ний днев­ной за­ра­бо­ток рас­счи­ты­ва­ет­ся за 2 ка­лен­дар­ных года, пред­ше­ству­ю­щих году на­ступ­ле­ния нетру­до­спо­соб­но­сти.", reply_markup=menu)

if __name__== '__main__':
   executor.start_polling(dp, skip_updates=True)