from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv()
def gpt_prompt(text, client, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model, 
        messages=text,
        stream=True  # again, we set stream=True
    )

    return completion

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
modelName = 'ft:gpt-3.5-turbo-1106:personal::8gtV0Nu9'

def gptPrompt(new_info):
    old_md = open('../transcription/output.md', 'r').read()
    current_text = open('../transcription/transcript.txt', 'r').read()

    prompt = f"""
    CURRENT MARKDOWN: {old_md}
    CURRENT INFORMATION: {current_text}
    NEW INFORMATION: {new_info}
    """
    print(prompt)
    message_data = [
        {"role": "system", "content": "You are studentGPT. Your task is to convert new information to short notes using markdown. Only add information that isn't written down in the markdown already"},
        {"role": "user", "content": prompt}
    ]

    completion = gpt_prompt(message_data, client, modelName)

    collected_chunks = []

    for chunk in completion:
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk.choices[0].delta.content  # extract the message
        if chunk_message is None:
            continue
        # Append chunk message to a markdown file
        with open("../transcription/output.md", "a") as file:
            file.write(str(chunk_message))
            print(chunk_message, end="")