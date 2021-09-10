import os, asyncio, toml
from functions import flood, join

for filename in os.listdir("sessions"):
    os.remove(os.path.join(
    "sessions", filename))

with open("config.toml") as file:
    config = toml.load(file)
authorization = config["authorization"]

update = input("update sessions?
sessions = os.listdir("sessions")
api_id, api_hash = authorization["api_id"], authorization["api_hash"]

while True:
    
