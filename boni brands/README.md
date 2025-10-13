# Telegram Weather & Stocks Bot (n8n)

**Test task for a programmer position.**

The bot runs on the [n8n.io](https://n8n.io) platform and can perform two functions:

1. Report the weather in a specified city.
2. Show the current stock prices of NASDAQ companies.

All user actions are logged in a Google Sheet.

---

## Functionality

### Weather
The user submits the name of the city—the bot reports the temperature and advises whether to wear a jacket.

- If the temperature is below 15°C → the bot says:
`Today is {{temperature}} degrees, it's cold, put on a jacket.`
- If it's 15°C or higher →
`Today is {{temperature}} degrees, it's a nice day, you can run in a t-shirt.`

API: [WeatherAPI](https://www.weatherapi.com/api-explorer.aspx)

---

### Stock Price
The user submits the company name or ticker symbol – the bot returns the current stock price on NASDAQ.

API: [Yahoo Finance via RapidAPI](https://rapidapi.com/apidojo/api/yahoo-finance1)

---

## Error Handling
The bot correctly:
- detects when something unrecognizable is entered (neither a city nor a company)
- responds: "Unable to identify the request. Try again."

---

## Logging
All requests and responses are logged in a Google Sheet:
- Date and time
- Entered text
- Request type (weather/stocks/error)
- Bot response

---

## Technologies

- [n8n Cloud](https://n8n.io)
- Telegram Bot API
- WeatherAPI
- Yahoo Finance (RapidAPI)
- Google Sheets Integration

---

## Installation and Launch

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Register with [WeatherAPI](https://www.weatherapi.com/)
3. Get an API key from [RapidAPI (Yahoo Finance)](https://rapidapi.com/apidojo/api/yahoo-finance1)
4. Create a Google Sheet with with the required columns (`ChatId`, `Question`, `Reply`)
5. Import `workflow.json` into n8n
6. Configure variables and credentials:
- Telegram Bot Token
- WeatherAPI Key
- RapidAPI Key + Host
- Google Sheets Access

---

## Usage Example

**User:** `London`
**Response:** `It's 12 degrees today, cold, put on a jacket.`

**User:** `AAPL`
**Response:** `The current AAPL stock price is $184.97`
