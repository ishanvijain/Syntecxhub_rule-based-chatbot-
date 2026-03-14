import re
import datetime

# --- 1. Knowledge Base (Domain Questions) ---
# You can expand this dictionary to answer more specific questions
knowledge_base = {
    "hours": "We are open from 9 AM to 5 PM, Monday to Friday.",
    "location": "Our main office is located at 123 Tech Lane, Silicon Valley.",
    "contact": "You can reach support at support@company.com or call 555-0199.",
    "duration": "The internship program lasts 6 months and focuses on AI development."
}

# --- 2. Intent Rules (Pattern Matching) ---
# Patterns use Regex: r"phrase1|phrase2" means "if user says phrase1 OR phrase2"
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

    # Step A: Check General Intents (Greetings/Small Talk)
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    # Step B: Check Knowledge Base (Domain Questions)
    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key]

    # Step C: Fallback
    return "I'm not sure about that. Could you try asking about our 'hours' or 'location'?"

# --- 3. The Interactive Console ---
print("--- InternBot 1.0 (Type 'bye' to quit) ---")

while True:
    user_msg = input("You: ")
    
    # Get the response
    bot_msg = get_response(user_msg)
    
    # Show the response
    print(f"Bot: {bot_msg}")
    
    # Log the history
    log_conversation(user_msg, bot_msg)
    
    # Break the loop if the user says goodbye
    if re.search(r"bye|goodbye", user_msg.lower()):
        break