import markovify
import json
import os

def learn_from_logs():
    with open("data/messages.json", encoding="utf-8") as f:
        lines = f.readlines()

    texts = [json.loads(line)["content"] for line in lines if line.strip()]
    model = markovify.NewlineText("\n".join(texts), state_size=2)

    os.makedirs("data/models", exist_ok=True)
    with open("data/models/global.json", "w", encoding="utf-8") as f:
        f.write(model.to_json())
