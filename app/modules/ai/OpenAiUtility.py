import openai
import json


class OpenAiUtility:
    def __init__(self):
        self.is_api_key_set = False
        self.prompts = []

    def init_open_ai(self, api_key):
        openai.api_key = api_key
        self.is_api_key_set = True

    def chat(self, prompt):
        if not self.is_api_key_set:
            raise Exception("OpenAI API key is not set")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"],
        )
        return json.loads(str(response))["choices"][0]["text"]

    def chatPlus(self, prompt):
        # print("ChatPlus: " + prompt)
        while len(self.prompts) > 2:
            self.prompts.pop(0)

        if not self.is_api_key_set:
            raise Exception("OpenAI API key is not set")
        self.prompts.append({"role": "user", "content": prompt})
        # print("Prompts: " + str(self.prompts))
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.prompts
        )

        # print(completion)

        return completion.choices[0].message["content"]

    def chatPlusSingle(self, prompt):
        # print("Prompts: " + str(self.prompts))
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=prompt
        )
        # print(completion)
        return completion.choices[0].message["content"]
