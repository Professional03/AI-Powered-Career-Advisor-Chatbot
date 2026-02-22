def update_chat_history(chat_history,user_message,bot_response):
    
    chat_history.append(f"User: {user_message}")
    chat_history.append(f"Guru: {bot_response}")

    return chat_history