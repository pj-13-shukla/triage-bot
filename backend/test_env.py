# test_env.py → check if all installed libraries are working

try:
    import fastapi
    import uvicorn
    import pydantic
    import dotenv
    import httpx
    import requests
    import loguru
    import sqlite3
    import google.generativeai as genai
    import langdetect
    import vosk
    import soundfile
    import gtts
    import pyttsx3
    import redis

    print("✅ All libraries imported successfully!")

except Exception as e:
    print("❌ Error:", e)
