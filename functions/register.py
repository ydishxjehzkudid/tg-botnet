from telethon.sync import TelegramClient

def main(api_id, api_hash):
    phone = input("[?] phone number ➜ ")
    session = phone.replace("+", "")
    client = TelegramClient(session,
    api_id, api_hash)
    print("[!] sending verify code")
    client.sign_in(phone)
    code = input("[?] verify code ➜ ")
    client.sign_in(phone, code)
