from dotenv import load_dotenv
import scratchattach as sa
from mcpq import Minecraft, Vec3
import os, base64

load_dotenv()
mc = Minecraft()
session = sa.login_by_id(os.getenv("SESSION_ID"), username=os.getenv("USERNAME"))
cloud = session.connect_cloud(os.getenv("PROJECT_ID"))
client = cloud.requests()

@client.request
def ping():
    print("Ping request received")
    return "pong"

@client.request
def post_to_chat(message):
    mc.postToChat(base64.b64decode(message + "===").decode("ascii"))
    return "ok"

@client.event
def on_ready():
    print("Request handler is ready")

def on_chat(event):
    client.send(base64.b64encode(f"<{event.player.name}> {event.message}".encode("ascii")).decode("ascii"))

mc.events.chat.register(on_chat)
client.start(thread=True)
