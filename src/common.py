from azure.identity import AzureCliCredential, get_bearer_token_provider
from openai import AzureOpenAI

chat_resource_tenant_id = '7b33e762-00b4-4e51-97a0-26e09d6c78de'
chat_resource_scope = 'https://cognitiveservices.azure.com/.default'
chat_resource_endpoint = 'https://azureaihub6334278155.cognitiveservices.azure.com/'
chat_resource_api_version = '2024-02-01'

def create_token_provider():
    return get_bearer_token_provider(AzureCliCredential(tenant_id=chat_resource_tenant_id), chat_resource_scope)

client = AzureOpenAI(
    azure_endpoint = chat_resource_endpoint,
    azure_ad_token_provider = create_token_provider(),
    api_version = chat_resource_api_version
    )

api_model = 'gpt-4o-mini'

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

if __name__ == '__main__':
    response = client.chat.completions.create(
        model=api_model,
        messages=[{ "role":"user", "content":"Hi!" }])
    print(response.choices[0].message.content)