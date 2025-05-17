import markovify
import os

class MarkovManager:
    def __init__(self):
        self.model = None
        self.model_path = "data/models/global.json"
        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "r", encoding="utf-8") as f:
                self.model = markovify.NewlineText.from_json(f.read())
        else:
            self.model = None

    def save_model(self):
        if self.model:
            os.makedirs("data/models", exist_ok=True)
            with open(self.model_path, "w", encoding="utf-8") as f:
                f.write(self.model.to_json())

    def learn(self, new_text: str):
        if not new_text.strip():
            return

        new_model = markovify.NewlineText(new_text, state_size=2)
        self.model = (
            markovify.combine([self.model, new_model])
            if self.model
            else new_model
        )
        self.save_model()

    def generate(self):
        if not self.model:
            return "まだよくわかんないよ…"
        return self.model.make_sentence(tries=100)
