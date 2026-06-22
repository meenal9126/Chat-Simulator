
import re
import ollama

# 1. Read the raw text
with open("chat.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# 2. Clean the text using a Regex pattern
# This matches common WhatsApp formats like "[12/05/26, 14:32:01]" or "12/05/26, 2:32 PM - "
clean_pattern = r'^\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?[ap]m\s-\s'
cleaned_text = re.sub(clean_pattern, '', raw_text, flags=re.IGNORECASE | re.MULTILINE)
chat_context=cleaned_text[:3000]

friend_name="Chatbot Simulator"

system_instruction = f"""
You are simulating a chat with a person named {friend_name}. 
Carefully study the texting style, slang, lowercase/uppercase habits, and emoji usage in the chat history provided below. 
You must respond EXACTLY like {friend_name} would. Keep your responses short, casual, and informal. Do not act like an AI assistant.

CHAT HISTORY CONTEXT:
{chat_context}
"""

#Inititalizing live conversation
live_convo=[
    {"role":"system", "content":system_instruction}
]

print(f"Chat Simulator ready! Talking to {friend_name} AI")
print("type your message and press 'Enter'. Type 'Quit' to exit.\n")

#INITIALIZING LOOP
while True:
    user_msg=input("YOU: ")
    if user_msg.lower=="quit":
        print("Closing Chat simulator. Bye!")
        break

    live_convo.append({"role":"user", "content":user_msg})

    response=ollama.chat(
        model="llama3",
        messages=live_convo
    )

    ai_reply=response['message']['content']

    #Printing what the AI Clone said
    print(f"{friend_name}: {ai_reply} \n")
    live_convo.append({"role":"assistant","content":ai_reply})
