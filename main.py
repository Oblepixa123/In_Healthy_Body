import telebot
import os
from dotenv import load_dotenv


load_dotenv()
token_user = os.getenv("TOKEN")
bot = telebot.TeleBot(token_user)
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("посчитать имт")

 
@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(
        message.from_user.id,
        f"Привет, {message.from_user.first_name}! Я телеграмм-бот для твоего здоровья!",

        reply_markup=keyboard)


@bot.message_handler(func=lambda message:True)
def get_body_index(message):
    try:
        nums = message.text.split()
        height = float(nums[0])
        weight = float(nums[1])
        body_index = (weight / height**2)
        get_body_indicators(body_index, message)
    except ValueError:
        bot.send_message(message.from_user.id, "Пожалуйста, введите рост и вес через пробел рост должен быть в метрах напимер(1.75) вес должен быть в киллограмах например (42).")# Здесь необходимо описать что будет происходить, при наступлении события "Ошибка значения"
        if len(nums) != 2:
          raise ValueError
           

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


if __name__ == "__main__":
  bot.polling(none_stop=True)