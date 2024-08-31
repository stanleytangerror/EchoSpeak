# EchoSpeak

A GPT-enhanced English practising experience.

## How to use

1. Install python dependencies:
 - `py -m pip install AzureOpenAI`
 - `py -m pip install requests`
 - `py -m pip install bottle`

2. Add environment variables:

 - `AZURE_OPENAI_ENDPOINT`: the azure AI endpoint, e.g., `https://<your_azureai_name>.openai.azure.com/`
 - `AZURE_OPENAI_API_KEY`: the access key
 - `AZURE_OPENAI_API_VERSION`: the api version, e.g., `2024-02-01`
 - `AZURE_OPENAI_MODEL`: the model deployment name, e.g., `gpt-4o`

3. Launch the server: `python .\src\server.py`

4. Open http://localhost:8080 in Chrome