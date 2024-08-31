import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"))

api_model = os.getenv("AZURE_OPENAI_MODEL")

native_speaker_prompt = """
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
"""
