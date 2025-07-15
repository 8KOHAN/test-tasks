import openai
from config import OPENAI_API_KEY, OPENAI_MODEL

openai.api_key = OPENAI_API_KEY

async def ask_gpt(messages: list[dict]) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"[GPT ERROR] {e}")
        return "Вибачте, виникла помилка при зверненні до AI 😓"
