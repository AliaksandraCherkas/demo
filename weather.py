import telebot
import requests
import json
TOKEN  = '7044178403:AAF89uml4qwcSE6W3-RtstHYpi_63eWtNBk'
bot = telebot.TeleBot(TOKEN)
API = '190037ba7478f5bc947729c365afcc64'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hello man')

@bot.message_handler(content_types=['text'])
def start(message):
    city = message.text.strip().lower()
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    
    data = json.loads(req.text)
    
    bot.reply_to(message, f"There are {data['main']['temp']} C-degrees in {city.capitalize()}")


    if req.status_code == 200:
         data = json.loads(req.text)
         bot.reply_to(message, f"There are {data['main']['temp']} C-degrees in {city.capitalize()}")
     else:
         bot.reply_to(message, 'non-existent city')






bot.polling(none_stop=True)

#for git-demo
