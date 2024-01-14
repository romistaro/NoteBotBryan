from pathlib import Path

from openai import OpenAI
from FineTuning.test import gptPrompt
import os


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



def stt(filename):
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

    audio_file= open(filename, "rb")
    transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
    )
    with open(dir_path / "transcript.txt", "a") as file:
        file.write(transcript.text + "\n")
    gptPrompt(transcript.text)
    
    
    


    



