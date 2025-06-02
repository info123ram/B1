from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from username_generator import generate_usernames
from telegram_sender import send_available_usernames
import config
import asyncio
import os

# Store session in 'session/' directory
session_dir = os.path.join(os.path.dirname(__file__), "session")
os.makedirs(session_dir, exist_ok=True)

session_file = os.path.join(session_dir, "ravi")

client = TelegramClient(session_file, config.API_ID, config.API_HASH)

async def check_usernames():
    await client.start(phone=config.PHONE)
    if await client.is_user_authorized() is False:
        await client.send_code_request(config.PHONE)
        try:
            await client.sign_in(config.PHONE, input("📲 Enter the OTP sent to your Telegram: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("🔐 Enter your 2FA password: "))

    print("✅ Logged in successfully")

    usernames = generate_usernames(500)  # Change this to 100000 in full run
    available = []

    for username in usernames:
        result = await client(functions.account.CheckUsernameRequest(username))
        if result:
            print(f"✅ Available: {username}")
            available.append(username)
            await send_available_usernames(username)
        else:
            print(f"❌ Taken: {username}")

    print("🎉 Done checking. Available:", available)

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(check_usernames())
