import os
import telebot
from messages import get_message
from services import get_air_quality_data, format_last_updated

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='html')


def generate_air_quality_message(city, air_quality_info):
    aqi = air_quality_info['main']['aqi']
    components = air_quality_info['components']

    response = f"<b>Air Quality in {city.capitalize()}:</b>\n"
    response += f"<b>Air Quality Index (AQI):</b> {aqi} - {get_aqi_index(aqi)}\n"
    response += "<b>Pollutant Levels:</b>\n"

    for pollutant, value in components.items():
        response += f"{pollutant.capitalize()}: {value} µg/m³\n"

    response += f"<b>Last Updated:</b> {format_last_updated(air_quality_info['dt'])}"

    return response


def get_aqi_index(aqi):
    if 0 <= aqi < 20:
        return "Good"
    elif 20 <= aqi < 80:
        return "Fair"
    elif 80 <= aqi < 250:
        return "Moderate"
    elif 250 <= aqi < 350:
        return "Poor"
    else:
        return "Very Poor"


def handle_air_quality_message(city, air_quality_data):
    if air_quality_data and 'list' in air_quality_data:
        air_quality_info = air_quality_data['list'][0]
        response = generate_air_quality_message(city, air_quality_info)
    else:
        response = get_message('error').format(city=city.capitalize())

    return response


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, get_message('welcome'))


@bot.message_handler(func=lambda message: True)
def get_air_quality(message):
    city = message.text
    air_quality_data = get_air_quality_data(city)
    response = handle_air_quality_message(city, air_quality_data)
    bot.reply_to(message, response)


@bot.message_handler(content_types=['location'])
def location_handler(message):
    location = message.location
    air_quality_data = get_air_quality_data((location.latitude,
                                            location.longitude))
    response = handle_air_quality_message('the provided location', 
                                          air_quality_data)
    bot.reply_to(message, response)


if __name__ == "__main__":
    bot.infinity_polling()
