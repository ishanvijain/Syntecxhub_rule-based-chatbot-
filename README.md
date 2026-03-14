# Syntecxhub_rule-based-chatbot-
A Python-based conversational agent that uses Pattern Matching and a Knowledge Base to interact with users.
Intent Recognition: Uses Regular Expressions (Regex) to identify user intents like greetings, help requests, and small talk.
Domain Knowledge Base: A built-in dictionary that allows the bot to answer specific questions about office hours, location, and services.
Persistent Logging: Automatically records every conversation with timestamps into a history.log file.
Input Normalization: Processes user input to be case-insensitive and clean of extra whitespace for better accuracy.

How It Works:
The bot follows a simple decision-making pipeline:
Capture: Receives string input from the console.
Clean: Converts text to lowercase and strips punctuation.
Match: Checks the input against predefined Regex patterns.
Lookup: If no pattern matches, it searches the Knowledge Base for keywords.
Log: Saves the interaction to a local text file.
