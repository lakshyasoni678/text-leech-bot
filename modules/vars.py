import os

API_ID    = os.environ.get("API_ID", "29640188")
API_HASH  = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6513312964:AAFYN_CVZ9PyeQi7v4jLkMRt-UDIHrqN6Ks") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
