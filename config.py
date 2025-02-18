import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Print a warning if the key is missing
if not OPENAI_API_KEY:
    print("⚠️ Warning: OPENAI_API_KEY is missing in the .env file!")
