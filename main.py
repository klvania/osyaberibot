import discord
from learning import learn_from_logs
from generator import generate_response
from scheduler import start_scheduler
import json
import os
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
MESSAGE_LOG = "data/messages.json"

@client.event
async def on_ready():
    print(f"✅ Bot起動完了: {client.user}")
    start_scheduler(client)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # 発言ログ保存
    os.makedirs("data", exist_ok=True)
    with open(MESSAGE_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "content": message.content
        }, ensure_ascii=False) + "\n")

    # ランダムで発言（例：40%）
    if random.random() < 0.4:
        response = generate_response()
        await message.channel.send(response)

    # 管理者再学習トリガー
    if message.content == "!learn":
        learn_from_logs()
        await message.channel.send("🧠 ふんふん、いっぱい覚えたよっ！")
