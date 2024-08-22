import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01")
    
deployment_name='gpt-4o' 
    
print('Sending a test completion job')
messages = [{"role":"user","content":"hi "}]
response = client.chat.completions.create(model=deployment_name, messages=messages, max_tokens=10)
print(response.choices[0].message.content)