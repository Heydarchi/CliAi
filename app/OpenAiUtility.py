import openai
import json


class OpenAiUtility:
    def __init__(self):
        self.is_api_key_set = False

    def init_open_ai(self, api_key):
        openai.api_key = api_key
        self.is_api_key_set = True

    def chat(self, prompt):
        if not self.is_api_key_set:
            raise Exception("OpenAI API key is not set")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Explain about secure coding",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )
        return json.loads(str(response))["choices"][0]["text"]

    def chatPlus(self, prompt):
        if not self.is_api_key_set:
            raise Exception("OpenAI API key is not set")
        OpenAiUtility.init_open_ai()
        completion = openai.ChatCompletion.create(
            model="gpt-4", messages=[{"role": "user", "content": prompt}]
        )

        return completion.choices[0].message["content"]
