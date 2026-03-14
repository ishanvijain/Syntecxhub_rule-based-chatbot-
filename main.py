import re
import datetime

knowledge_base = {
    "hours": "We are open from 9 AM to 5 PM, Monday to Friday.",
    "location": "Our main office is located at 123 Tech Lane, Silicon Valley.",
    "contact": "You can reach support at support@company.com or call 555-0199.",
    "duration": "The internship program lasts 6 months and focuses on AI development."
}

rules = {
    r"hello|hi|hey": "Hello! I'm your bot. Type 'help' for assistance?",
    r"help|support": "I can answer questions about our hours, location, duration or contact info.",
    r"how are you|how's it going": "I'm functioning at 100% capacity! How about you?",
    r"who made you|creator": "I was created as a Project 1 assignment for an internship.",
    r"thanks|thankyou|thank you|thank you so much":" Yes, No problem. It was great assisting your queries.",
    r"bye|goodbye|exit" : "Goodbye! It was nice chatting with you."
}

def log_conversation(user_text, bot_text):
   
    with open("chat_history.log", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] User: {user_text}\n")
        file.write(f"[{timestamp}] Bot: {bot_text}\n\n")

def get_response(user_input):
    user_input = user_input.lower().strip()

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key]

    return "I'm not sure about that. Could you try asking about our 'hours' or 'location'?"

print("--- InternBot 1.0 (Type 'bye' to quit) ---")

while True:
    user_msg = input("You: ")
    
    bot_msg = get_response(user_msg)
    
    print(f"Bot: {bot_msg}")
    
    log_conversation(user_msg, bot_msg)
    
    if re.search(r"bye|goodbye", user_msg.lower()):
        break