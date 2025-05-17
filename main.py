import discord
import json
import os
import random

from learning import MarkovManager
from generator import decorate_sentence
from scheduler import start_scheduler

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
markov = MarkovManager()

@client.event
async def on_ready():
    print(f"✅ Bot起動完了: {client.user}")
    start_scheduler(client, markov)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip()

    # 発言記録
    os.makedirs("data", exist_ok=True)
    with open("data/messages.json", "a", encoding="utf-8") as f:
        f.write(json.dumps({"content": content}, ensure_ascii=False) + "\n")

    # 学習（自動）
    markov.learn(content)

    # ランダムで返信（40%）
    if random.random() < 0.4:
        sentence = markov.generate()
        response = decorate_sentence(sentence)
        await message.channel.send(response)
