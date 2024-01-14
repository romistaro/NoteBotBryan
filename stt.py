from openai import OpenAI
import os


client = OpenAI(api_key="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")


def stt(filename):
    audio_file= open(filename, "rb")
    transcript = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
    )

    print(transcript.text)



