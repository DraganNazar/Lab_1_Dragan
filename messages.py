MESSAGES = {
    'welcome': "Hello! I am the Air Quality Bot. Send me the name of a city "
               "or location, and I will provide you with air quality information.",
    'error': "Sorry, I couldn't retrieve air quality information for {city}. "
             "Please try again.",
}


def get_message(message_key: str) -> str:
    return MESSAGES[message_key]