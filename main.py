import telebot#импорт библиотеки
import os#импорт библиотеки
from dotenv import load_dotenv#импорт функции из библиотеки


load_dotenv()#вызов функции load_dotenv
token_user = os.getenv("TOKEN")#переменная с токеном пользователя

bot = telebot.TeleBot(token_user)# Создаем экземпляр бота
keyboard = telebot.types.ReplyKeyboardMarkup(True)#переменная с созданием кнопки для пользователя
keyboard.row("посчитать имт")#row с надписью на кнопке пользователя

 

#@bot.message_handler(commands=["start"])
#def start_messages(message):
    #user_massage = "Привет "+ message.from_user.first_name +" я телеграм бот для твоего здоровья"
    #bot.send_message(message.from_user.id, user_massage)

#@@bot.message_handler(content_types=["text"])
#def handle_text(message):
    #bot.send_message(message.from_user.id, 'Вы написали: ' + message.text)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(
        message.from_user.id,
        f"Привет, {message.from_user.first_name}! Я телеграмм-бот для твоего здоровья!",

        reply_markup=keyboard)

@bot.message_handler(func=lambda message:True)#Создаем обработчик события, ожидающий сообщение пользователя
def get_body_index(message):#фуекция просчитывающая индекс массы тела по введеным пользователем данным
    try:
        nums = message.text.split()# с помощью функции сплит разделаем числа введеные пользователем которые хранятса в переменной нумс
        height = float(nums[0])#обращаемся к числам по их индексу 
        weight = float(nums[1])#обращаемся к числам по их индексу 
        body_index = (weight / height**2)#считаем индекс массы тела по формуле
        get_body_indicators(body_index, message)
      

       
    except ValueError:#анализ исключений
        bot.send_message(message.from_user.id, "Пожалуйста, введите рост и вес через пробел рост должен быть в метрах напимер(1.75) вес должен быть в киллограмах например (42).")# Здесь необходимо описать что будет происходить, при наступлении события "Ошибка значения"
        if len(nums) != 2:#с помощью функции лен оперделяем есть ли в строчке 2 элемента
          raise ValueError#если в строчке не двух элемента то вызываем исключение
           
#функция с условиями определяющими имт по введеным пользователем данным
def get_body_indicators(index_body_mass, message):
    if index_body_mass < 16:
      bot.send_message(message.from_user.id, "выраженный дефицит массы тела.") 
    elif index_body_mass >= 16 and index_body_mass <= 18.5:
      bot.send_message(message.from_user.id,"дефицит массы")
    elif index_body_mass >= 18.5 and index_body_mass <= 25:
      bot.send_message(message.from_user.id,"норма")
    elif index_body_mass >= 25 and index_body_mass <= 30:
      bot.send_message(message.from_user.id,"избыточная масса тела")
    elif index_body_mass >= 30 and index_body_mass <= 35:
      bot.send_message(message.from_user.id,"1 степень ожирения")
    elif index_body_mass >= 35 and index_body_mass <= 40:
      bot.send_message(message.from_user.id,"2 степень ожирения")
    elif index_body_mass > 40:
      bot.send_message(message.from_user.id,"3 степень ожирения")


 #   weight = float(input("какой у вас вес в килограммах? "))
 #   height = float(input("какой у вас рост в метрах? "))
 # index = round(weight / height**2)
 #  get_body_index (index)




if __name__ == "__main__":
  bot.polling(none_stop=True)#запускаем бота чтобы он прослушивал события и реагировал на них без остановки