import datetime
import os

LOG_FILE_PATH = "logs/chat_logs.txt"

def log_chat(user_input, ai_response):
    """Logs user input and AI response to a file."""
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] User: {user_input}\n")
        log_file.write(f"[{timestamp}] AI: {ai_response}\n\n")

def clear_logs():
    """Clears the chat log file."""
    open(LOG_FILE_PATH, "w").close()
