from openai import OpenAI
from test import gptPrompt
import os


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



def stt(filename):
    audio_file= open(filename, "rb")
    transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
    )
    
    gptPrompt(transcript.text)
    
    
    
    with open("transcript.txt", "a") as file:
        file.write(transcript.text + "\n")

    



