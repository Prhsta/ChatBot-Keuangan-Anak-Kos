from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("💸 Chatbot Keuangan Anak Kos")
print("Ketik 'exit' untuk berhenti\n")

while True:
    user_input = input("Kamu: ")

    if user_input.lower() == "exit":
        print("Chatbot: Semoga keuanganmu makin rapi ya! 👋")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.6,
        max_tokens=500
    )

    reply = response.choices[0].message.content
    print(f"Chatbot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
