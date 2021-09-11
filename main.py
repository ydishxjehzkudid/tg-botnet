import os, asyncio, toml
from functions import flood, join
from functions import register

for filename in os.listdir("sessions"):
    if filename.endswith(".session-journal"):
        os.remove(os.path.join(
        "sessions", filename))

with open("config.toml") as file:
    config = toml.load(file)["sessions"]

api_id, api_hash = config["api_id"], config["api_hash"]

update = input("update sessions ➜ ")
if update.lower() in ["y", "yes", "ye"]:
    register(api_id=api_id,
    api_hash=api_hash)

sessions = os.listdir("sessions")
print("total accounts ➜ %d" % len(sessions))

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
            "2) raid with file\n"\
            "3) raid with mention\n"
            while True:
                try:
                    action = int(input("➜ "))
                    trigger = input("trigger ➜ ")
                    if action == 1:
                        print("Running accounts...")
                        for acc in sessions:
                            flood.ChatText(name=acc, api_id=api_id,
                            api_hash=api_hash, trigger=trigger).start()
                        print(f"Send «{trigger}» to chat!")
                    elif action == 2:
                        file = input("file ➜ ")
                        print("Running accounts...")
                        for acc in sessions:
                            flood.ChatFile(name=acc, api_id=api_id,
                            api_hash=api_hash, trigger=trigger, file=file).start()
                        print(f"Send «{trigger}» to chat!")
                    elif action == 3:
                        pass
                    elif True:
                        print(f"Invalid option «{action}»")
                except:
                    pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        elif True:
            print(f"Invalid option «{action}»")
