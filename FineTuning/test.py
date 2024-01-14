from openai import OpenAI
from dotenv import load_dotenv
import os

def gpt_prompt(text, client, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model, 
        messages=text,
    )

    return completion.choices[0].message.content

load_dotenv()
api_key = os.environ.get("API_KEY")
client = OpenAI(api_key=api_key)
modelName = 'ft:gpt-3.5-turbo-1106:personal::8gkyEzju'

prompt = """
CURRENT MARKDOWN:
CURRENT INFORMATION:
NEW INFORMATION: Python was invented in February 20, 1991. It is
"""

message_data = [
    {"role": "system", "content": "You are studentGPT. Your task is to convert new information to short notes using markdown. Only add information that isn't written down in the markdown already"},
    {"role": "user", "content": prompt}
]

completion = gpt_prompt(message_data, client, modelName)
print(completion)
