import markovify
import random
import json
import os

def generate_response():
    try:
        with open("data/models/global.json", encoding="utf-8") as f:
            model = markovify.NewlineText.from_json(f.read())

        sentence = model.make_sentence(tries=100)
        if not sentence:
            return "うーん…わかんないや…"

        # ポンコツ語尾
        suffix_pool = ["にゃ", "だぞ〜", "なのだ！", "うぇ〜い", "だと思うの", "やばば", "うむうむ"]
        suffix = random.choice(suffix_pool)

        return sentence + " " + suffix

    except Exception as e:
        print(f"[ERROR] Generate: {e}")
        return "え〜っと…なに話してたっけ…"
