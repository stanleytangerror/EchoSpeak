from common import *
import time
 
class Chat:
    chat_prompt = """
Your are a native speaker.

Remenber:
- Please keep it as conversational as possible, not too formal.
"""

    history=[
            { "role":"system", "content": native_speaker_prompt },
            { "role":"system", "content": chat_prompt }
        ]

    def chat(self, message):
        start_time = time.time()
        self.history.append({ "role":"user", "content":message })

        response = client.chat.completions.create(
            model='gpt-4o',
            messages=self.history,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0)
   
        reply = response.choices[0].message.content
        self.history.append({ "role":"assistant", "content":reply })

        print(f"[Profile] chat: {time.time() - start_time:.2f}")
        return reply

if __name__ == '__main__':
    print(Chat().chat('Hi, it is sunny outside!'))