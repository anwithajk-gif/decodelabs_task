# Project 1: Rule-Based AI Chatbot
# Uses dictionary (hash map) for O(1) intent matching

responses = {
    'hello': 'Hi there!',
    'hi': 'Hello! How can I help you?',
    'hey': 'Hey! What\'s up?',
    'how are you': 'I am doing great, thanks for asking!',
    'what is your name': 'I am a rule-based chatbot.',
    'who are you': 'I am a simple AI assistant built using if-else logic and dictionaries.',
    'what can you do': 'I can respond to predefined inputs using rule-based matching.',
    'help': 'Try: hello, how are you, what is your name, bye, exit',
    'bye': 'Goodbye!',
    'goodbye': 'See you later!',
}

print("Rule-Based Chatbot Started!")
print("Type 'exit' to quit\n")

while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    
    if clean_input == 'exit':
        print("Bot: Goodbye!")
        break
    
    reply = responses.get(clean_input, "I don't understand that.")
    print(f"Bot: {reply}")