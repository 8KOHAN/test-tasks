# NeuroTalk — AI Manager in Telegram

**NeuroTalk** is a Telegram bot for a laser epilation specialist that chats with clients, answers questions, and helps book procedures via Google Calendar.

---

## Features

### AI Manager
- Communicates in Ukrainian.
- Automatically handles frequently asked questions (FAQ).
- Responds to common objections: "Does it hurt?", "Too expensive", "From what age?" and more.
- Simulates realistic communication on behalf of the specialist.

### Google Calendar Booking
- The bot shows **available time slots** (taking busy events into account).
- Once the client selects a time — an **event is created** with status `busy`.
- The client receives a confirmation:  
  _"Appointment confirmed ✅ See you on DD.MM at HH:MM"_

---

## 🛠Technologies

- `Python 3.10+`
- `Aiogram` 
- `Google Calendar API` + `Service Account`
- `gemma:7b` (LLM)

---

## Project Structure

```bash
NeuroTalk/
├── bot/
│ ├── main.py # bot entry point
│ ├── handlers/ # message handlers
│ └── prompts/ # system_prompt for LLM
├── services/
│ └── calendar_client.py # Google Calendar integration
├── .env # environment variables
├── credentials.json # Google Service Account key
└── README.md
```
