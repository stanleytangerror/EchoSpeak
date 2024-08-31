from common import *
import time
import pprint

class Expression:
    system_prompt = """
Your job is to give a more natural and oral way to express the conversation.

Remember:
- Please only refine the last expression from "user", never refine someone else's expression.
- Please provide the optional expression only, do not return any other extra words.
- The better expression should be as conversational as possible, just like what native speaker does, never be too formal.
"""

    def refine(self, conversation):
        start_time = time.time()

        latest_conversation = conversation[-4:]

        while latest_conversation[-1]['role'] != 'user':
            latest_conversation.remove(latest_conversation[-1])

        if len(latest_conversation) == 0:
            raise ValueError

        history = [f"- {msg['role']}: {msg['content']} \n" for msg in latest_conversation]

        next_prompt = "Here is our conversation:\n\n" + '\n'.join(history)

        messages=[
            { "role":"system", "content": native_speaker_prompt },
            { "role":"system", "content": self.system_prompt },
            { "role":"user", "content": next_prompt }
        ]

        # pprint.pp(messages)

        response = client.chat.completions.create(
            model='gpt-4o',
            messages=messages,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0)
       
        reply = response.choices[0].message.content

        print(f"[Profile] refine: {time.time() - start_time:.2f}")
 
        return reply

if __name__ == '__main__':

    conversation = [
        { "role":"user", "content":'Hi, it is pretty sunny outside' },
        { "role":"assistant", "content":"Hey! Yeah, it's super nice out today. Perfect weather for a walk or something. Got any plans for the day?" },
        { "role":"user", "content":"No. But I'd like to go out. However, I don't know what to do." },
        { "role":"assistant", "content":"So many options! You could go for a walk or a bike ride." }
    ]

    print(Expression().refine(conversation))