from threading import Thread
import os, sys, asyncio
from telethon.sync import TelegramClient, events
from telethon import functions

class chat(Thread):
    def __init__(self, name, api_id, api_hash, trigger):
        self.name = "sessions/" + name
        self.api_id = api_id
        self.api_hash = api_hash
        self.trigger = trigger
        Thread.__init__(self)
    def main(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(session_name=self.name, api_id=self.api_id,
            api_hash=self.api_hash)
            client.connect()
        
            @client.on(events.NewMessage):
            async def flood(message):
                if message.text != self.trigger:
                    return
                count = 0
                while True:
                    try:
                        msg = await client(functions.messages.SendMessageRequest(
                        peer=message.chat_id, message="test")
                        count += 1
                        print(f"[{msg.sender_id}] sended [count: {count}]")
                    except Exception as error:
                        try:
                            me = message.client.get_me()
                            print(f"[{me.id}] not sended [error: {error}]")
                        except Exception as err:
                            print(str(error) + str(err))
            client.start()
            client.run_until_disconnected()
        except Exception as error:
            print(error)
