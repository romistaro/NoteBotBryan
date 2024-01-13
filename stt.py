from google.cloud import speech

client = speech.SpeechClient.from_service_account_file("astral-sorter-411120-6accb763bded.json")

def transcribe(f):
    with open(f, 'rb') as audio_file:
        mp3dat = audio_file.read()
    
    audio_file = speech.RecognitionAudio(content=mp3dat)

    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio_file)

    # Open the text file in append mode
    with open("transcription.txt", "a") as text_file:
        for result in response.results:
            # Extract the transcript from the first alternative
            transcript = result.alternatives[0].transcript
            # Write the transcript to the text file
            text_file.write(transcript + "\n")