# Air Quality Telegram Bot

This Telegram bot provides information about air quality in different locations.

## Features

- Get real-time air quality data for a specific city or location.
- Supports location-based queries using Telegram's location sharing feature.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install `pipenv` if you haven't already:
```bash
pip install pipenv
```
4. Install the project dependencies using pipenv:
```bash
pipenv install
```

5. Obtain an API token for the OpenWeatherMap API:

   * Go to the OpenWeatherMap website and sign up for an account.
   * Retrieve your API key.
6. Go to [@BotFather](https://telegram.me/botfather) on Telegram and create a new bot. Follow the instructions provided by BotFather to create your bot and obtain the API token.

7. Set up environment variables:
     ```
     export BOT_TOKEN=<YOUR_BOT_TOKEN>
     export API_KEY=<YOUR_API_KEY>
     ```
   *Replace `YOUR_BOT_TOKEN` and `YOUR_API_KEY` with your values
8. Launch the virtual environment:
```bash
pipenv shell
```
9. Start the bot:

```shell
python bot.py
```
## Usage
- Start the bot by sending `/start` or `/help` to get instructions.
- To get air quality information for a specific city, simply send the city name as a text message.
- Alternatively, you can share your location to get air quality information based on your current location.
## Contributing
Contributions to the Telegram Air Quality Bot are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
## License

[MIT](https://choosealicense.com/licenses/mit/)
* Author: Valentyn Stratii
