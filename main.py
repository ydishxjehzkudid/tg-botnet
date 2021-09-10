import os, asyncio, toml
from functions import flood, join

for filename in os.listdir("sessions"):
    if filename.endswith(".session-journal"):
        os.remove(os.path.join(
        "sessions", filename))

with open("config.toml") as file:
    config = toml.load(file)

authorization = config["authorization"]
api_id, api_hash = authorization["api_id"], authorization["api_hash"]

update = input("update sessions?
sessions = os.listdir("sessions")

while True:
    
