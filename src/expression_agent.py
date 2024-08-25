from common import *
import pprint

class Expression:
    system_prompt = """
Your job is to give me a more natural way to express what I meant in my last response.

Remember: 
- Please give me the optional expression only, do not return any other extra words.
- The better expression should be as conversational as possible, just like what native speaker does, never be too formal.
"""

    def refine(self, conversation):
        latest_conversation = conversation[-4:]

        if not any(msg['role'] == 'user' for msg in latest_conversation):
            raise ValueError

        history = [f"- {'Me' if msg['role'] == 'user' else 'Stan'}: {msg['content']} \n" for msg in latest_conversation]

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
        return reply

if __name__ == '__main__':

    conversation = [
        { "role":"user", "content":'Hi, it is pretty sunny outside' },
        { "role":"assistant", "content":"Hey! Yeah, it's super nice out today. Perfect weather for a walk or something. Got any plans for the day?" },
        { "role":"user", "content":"No. But I'd like to go out. However, I don't know what to do." }
    ]

    print(Expression().refine(conversation))