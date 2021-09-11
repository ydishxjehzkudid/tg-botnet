import os, asyncio, toml
from functions import flood, join
from functions import register

for filename in os.listdir("sessions"):
    if filename.endswith(".session-journal"):
        os.remove(os.path.join(
        "sessions", filename))

with open("config.toml") as file:
    config = toml.load(file)

authorization = config["authorization"]
api_id, api_hash = authorization["api_id"], authorization["api_hash"]

update = input("[?] update sessions ➜ ")
if update.lower() in ["y", "yes", "ye"]:
    register(api_id=api_id,
    api_hash=api_hash)

sessions = os.listdir("sessions")
print("[*] total accounts ➜ %d" % len(sessions))

menu = \
"1) flood to pm\n"\
"2) flood to chat\n"\
"3) join the chat\n"\
"4) change bio\n"

while True:
    try:
        action = int(input("➜ "))
        if action == 1:
            menu = \
            "1) raid with text\n"\
            "2) raid with reply\n"\
            "3) raid with gif\n"
            while True:
                try:
                    action = int(input("➜ "))
                    if action == 1:
                        pass
                    elif action == 2:
                        pass
                    elif action == 3:
                        pass
                    elif True:
                        print(f"[x] invalid option \"{action\"")
                except:
                    pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        elif True:
            print(f"[x] invalid option \"{action}\"")
