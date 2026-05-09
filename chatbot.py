
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "good morning", "good afternoon", "good evening"]:
        return "Hello! How can I assist you today?"
    
    elif user_input in ["how are you", "how are you doing"]:
        return "I am functioning well, thank you. How may I help you?"
    
    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple chatbot created to assist you with basic queries."

    elif user_input in ["help", "can you help me"]:
        return "Certainly! Please let me know how I can assist you."
    
    elif user_input in ["bye", "exit", "quit"]:
        return "Thank you for chatting. Have a great day!"
    
    else:
        return "I'm sorry, I did not understand your request. Could you please rephrase?"

print("Chatbot is now active. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    if user_input.lower() in ["bye", "exit", "quit"]:
        break