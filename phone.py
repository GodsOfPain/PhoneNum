# Mohamed Safeek

import telebot
import phonenumbers
from phonenumbers import timezone, carrier, geocoder

# Replace with your actual bot token
bot = telebot.TeleBot("5624652053:AAFA4kM1znARmBPSwY9TtBLI0AKNgmqC4IY")

# StartActivity
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Please enter your name.')

# Author  
@bot.message_handler(commands=['author'])
def send_hello(message):
    bot.send_message(message.chat.id, "Instagram: https://instagram.com/response.200")
    bot.send_message(message.chat.id, "Website: https://lone1177.blogspot.com/")
    bot.send_message(message.chat.id, "Telegram Group: https://t.me/lonemods")

# Whole Func
@bot.message_handler(func=lambda message:True)
def handle_contact(message):
    phone_number = message.text
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        country = phonenumbers.region_code_for_number(parsed_number)
        timeZone = timezone.time_zones_for_number(parsed_number)
        cArrier = carrier.name_for_number(parsed_number, "en")
        is_valid = phonenumbers.is_valid_number(parsed_number)
        if is_valid == "True":
        	is_valid="✅"
        else:
        	is_valid="❎"
        is_possible = phonenumbers.is_possible_number(parsed_number)
       
        response = f"Phone Number: {phone_number}\n"
        response += f"Country: {country}\n"
        response += f"Timezone: {timeZone}\n"
        response += f"Carrier: {cArrier}\n"
        response += f"Is Valid: {is_valid}\n"
        response += f"Is Possible: {is_possible}"
     
    except phonenumbers.phonenumberutil.NumberParseException:
        response = "Wrong input, please share a valid phone number."

    bot.reply_to(message, response)

# Start the bot
bot.polling()
