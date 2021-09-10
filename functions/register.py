from telethon.sync import TelegramClient
import os, sys

def main(api_id, api_hash):
    phone = input("[?] phone number ➜ ")
    session = phone.replace("+", "")
    client = TelegramClient(session,
    api_id, api_hash)
    print("[&] sending verify code")
    client.sign_in(phone)
    code = input("[?] verify code ➜ ")
    client.sign_in(phone, code)
    os.execl(sys.executable,
    sys.executable, *sys.argv) 
    return
