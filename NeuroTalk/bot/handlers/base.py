from aiogram import Router, types
from services.openai_client import ask_gpt
from dialog_state import add_to_history, dialog_history
from config import OPENAI_MODEL

router = Router()

SYSTEM_PROMPT = "Ти — віртуальний менеджер майстра лазерної епіляції..."

@router.message()
async def handle_user_message(message: types.Message):
    user_id = message.from_user.id
    user_text = message.text

    add_to_history(user_id, "user", user_text)

    history = dialog_history.get(user_id, [])
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    reply = await ask_gpt(messages)

    add_to_history(user_id, "assistant", reply)

    await message.answer(reply)
