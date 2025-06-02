from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl import functions
from username_generator import generate_usernames
from telegram_sender import send_available_usernames
import config
import asyncio
import os

# ✅ Create session folder
session_dir = os.path.join(os.path.dirname(__file__), "session")
os.makedirs(session_dir, exist_ok=True)

# ✅ Session file path (named 'ravi')
session_file = os.path.join(session_dir, "ravi")

# ✅ Telethon client setup
client = TelegramClient(session_file, config.API_ID, config.API_HASH)

async def check_usernames():
    # 🔐 Start client and request OTP
    await client.connect()
    if not await client.is_user_authorized():
        print("📲 Telegram OTP required...")
        await client.send_code_request(config.PHONE)

        try:
            code = input("📲 Enter the OTP sent to your Telegram: ")
            await client.sign_in(config.PHONE, code)
        except SessionPasswordNeededError:
            password = input("🔐 Enter your 2FA password: ")
            await client.sign_in(password=password)

    print("✅ Logged in successfully!")

    # 🔎 Generate usernames
    usernames = generate_usernames(500)  # Change to 100000 later
    available = []

    for username in usernames:
        try:
            result = await client(functions.account.CheckUsernameRequest(username))
            if result:
                print(f"✅ Available: {username}")
                available.append(username)
                send_available_usernames(username)
            else:
                print(f"❌ Taken: {username}")
        except Exception as e:
            print(f"⚠️ Error checking {username}: {str(e)}")

    print("🎉 Done checking. Total available:", len(available))

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(check_usernames())
