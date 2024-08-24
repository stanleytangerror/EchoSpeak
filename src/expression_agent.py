import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01")
    
system_prompt = """
Here are some characteristics of native speakers.
- Contractions and Informal Grammar: Frequent use of contractions like "can't," "won't," and "it's," as well as relaxed grammatical structures.
- Colloquial Vocabulary: Use of everyday words, slang, and idiomatic expressions.
- Casual Tone: Generally more relaxed, friendly, and conversational in nature.
- Flexible Syntax: More flexible sentence structures, often with less strict adherence to grammatical rules.
- Natural Pronunciation: Informal pronunciations, including reductions like "gonna" for "going to" and "wanna" for "want to."
- Pauses and Intonation: Relies heavily on natural pauses, intonation, and emphasis to convey meaning and emotion.
- Repetition and Fillers: Includes repetitions and filler words like "um," "uh," "like," and "you know."
- Interactive Nature: Often involves back-and-forth exchanges, interruptions, and immediate feedback from listeners.
- Shorter Sentences: Tends to use shorter, simpler sentences compared to written language.
- Context-Dependent: Heavily reliant on the context, body language, and shared knowledge between speakers.

Your job is to give me a more natural way to express what I meant in my last response.

Remember: 
- Please give me the optional expression only, do not return any other extra words.
- The better expression should be as conversational as possible, just like what native speaker does, never be too formal.
"""

conversation = """
Here is our conversation:

- Me: Hi, it is pretty sunny outside
- Stan: Hey! Yeah, it's super nice out today. Perfect weather for a walk or something. Got any plans for the day?
- Me: No. But I'd like to go out. However, I don't know what to do.
"""

response = client.chat.completions.create(
    model='gpt-4o', 
    messages=[
        { "role":"system", "content": system_prompt },
        { "role":"user", "content": conversation }
    ], 
    max_tokens=800,
    temperature=0.7, 
    top_p=0.95,
    frequency_penalty=0)
print(response.choices[0].message.content)