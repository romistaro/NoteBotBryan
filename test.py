from openai import OpenAI
import os


client = OpenAI(api_key="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")

audio_file= open("./f1.wav", "rb")
transcript = client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)
print(transcript)



