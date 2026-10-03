from openai import OpenAI

client = OpenAI()

with open("furia_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

post = input("Вставь текст поста: ")

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=system_prompt,
        input=f"""
Пост канала:
{post}

Напиши один комментарий Фурии.
"""
    )

    print("\nФурия:")
    print(response.output_text)

except Exception as e:
    print("\nОШИБКА API:")
    print(type(e).__name__)
    print(e)