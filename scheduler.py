from apscheduler.schedulers.asyncio import AsyncIOScheduler
from generator import decorate_sentence
import random

def start_scheduler(client, markov):
    scheduler = AsyncIOScheduler()

    @scheduler.scheduled_job("interval", minutes=10)
    async def random_talk():
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    if random.random() < 0.2:
                        sentence = markov.generate()
                        response = decorate_sentence(sentence)
                        await channel.send(response)
                        break

    scheduler.start()
