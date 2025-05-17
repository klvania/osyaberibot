from apscheduler.schedulers.asyncio import AsyncIOScheduler
from generator import generate_response
import random

def start_scheduler(client):
    scheduler = AsyncIOScheduler()

    @scheduler.scheduled_job("interval", minutes=10)
    async def random_talk():
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    if random.random() < 0.2:
                        response = generate_response()
                        await channel.send(response)
                        break

    scheduler.start()
