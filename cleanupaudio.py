from openai import OpenAI


client = OpenAI(
    api_key='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'
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": """
         correct any errors in this sample of human speech processed by a speech-to-text program. Use the context of the sentence to determine if certain words were transcribed incorrectly.
         ### Example Input ###

the quick frown fox jump over the lazy pog

### Example Output ###

The quick brown fox jumps over the lazy dog.
        """},
        {"role": "user", "content": "cats always scratch me. i ate cats"}
    ]
)

print(completion.choices[0].message)
