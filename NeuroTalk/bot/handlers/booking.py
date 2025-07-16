from aiogram import Router, types, F
from aiogram.filters import Command
from datetime import datetime, timedelta

from services.calendar import list_free_slots, create_appointment
from services.dialog_state import dialog_history, add_to_history
from utils.slot_parser import slots_to_text, is_valid_slot_choice
from utils.formatting import format_datetime_for_user

router = Router()

# Команда /booking або вручну викликана клавіша
@router.message(Command("booking"))
@router.message(F.text.lower() == "записатися")
async def handle_booking(message: types.Message):
    user_id = message.from_user.id
    now = datetime.utcnow()

    try:
        slots = list_free_slots(
            start_iso=now.isoformat(),
            end_iso=(now + timedelta(days=3)).isoformat(),
            duration_minutes=30
        )

        if not slots:
            await message.answer("На жаль, наразі немає вільних слотів. Напишіть, будь ласка, пізніше 🙏")
            return

        text = slots_to_text(slots)

        add_to_history(user_id, "system", "slots:" + str(slots))

        await message.answer(text + "\nНапишіть номер слота, який вам підходить 👇")

    except Exception as e:
        print(f"[BOOKING ERROR] {e}")
        await message.answer("Виникла помилка при отриманні слотів 😓")


# Вибір номера слота після /booking
@router.message(F.text.regexp(r"^\d+$"))
async def handle_slot_selection(message: types.Message):
    user_id = message.from_user.id
    user_text = message.text.strip()
    idx = int(user_text) - 1

    history = dialog_history.get(user_id, [])
    for entry in history:
        if entry["role"] == "system" and entry["content"].startswith("slots:"):
            try:
                slots = eval(entry["content"][6:])
                if not is_valid_slot_choice(user_text, slots):
                    await message.answer("Будь ласка, оберіть коректний номер слота 📋")
                    return

                idx = int(user_text) - 1
                start_iso, end_iso = slots[idx]

                create_appointment(
                    start_iso=start_iso,
                    end_iso=end_iso,
                    summary="Лазерна епіляція",
                    description=f"Запис через Telegram (ID {user_id})"
                )

                formatted_time = format_datetime_for_user(start_iso)
                await message.answer(f"Запис підтверджено ✅ Чекаємо вас {formatted_time}")
                return

            except Exception as e:
                print(f"[APPOINTMENT ERROR] {e}")
                await message.answer("Вибачте, сталася помилка при записі 😔")
            return
