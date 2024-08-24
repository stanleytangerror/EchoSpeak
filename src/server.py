from bottle import run, get, post, request
from chat_agent import Chat
from expression_agent import Expression

chatter = Chat()
refiner = Expression()

@get('/')
def index():
    return '<b>Hello world</b>!'

@post('/chat')
def chat():
    try:
        message = request.json['content']
    except:
        raise ValueError
    
    print(f'receive: \n{message}')
    reply = chatter.chat(message)
    refine = refiner.refine(chatter.history)
    return { 'refine': refine, 'reply': reply }

run(host='localhost', port=8080)