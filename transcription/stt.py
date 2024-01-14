from openai import OpenAI
import os


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



def stt(filename):
    audio_file= open(filename, "rb")
    transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
    )

    print(transcript.text)



