from telethon.sync import TelegramClient
import os, sys

def main(api_id, api_hash):
    phone = input("phone number ➜ ")
    session = str(len(os.listdir("sessions")))
    client = TelegramClient(session,
    api_id, api_hash)
    print("Sending verify code...")
    client.sign_in(phone)
    code = input("verify code ➜ ")
    client.sign_in(phone, code)
    return os.execl(sys.executable,
    sys.executable, *sys.argv) 
