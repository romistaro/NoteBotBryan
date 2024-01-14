from openai import OpenAI
from pathlib import Path
import os
from test import bryan

path = Path(os.path.dirname(os.path.realpath(__file__)))

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def stt(filename):
    audio_file = open(filename, "rb")
    transcript = client.audio.translations.create(
        model="whisper-1",
        file=audio_file
    )
    
    bryan(transcript.text)
    
    with open(path/"transcription.txt", "a") as file:
        file.write(transcript.text)
        print(transcript.text)
    
    
    
    
    
    

    



