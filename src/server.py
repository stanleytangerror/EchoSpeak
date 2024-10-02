import os
from bottle import run, get, post, request, static_file
from chat_agent import Chat
from expression_agent import Expression

chatter = Chat()
refiner = Expression()

@get('/')
def index():
    return static_file('site/index.html', root=os.path.dirname(os.path.abspath(__file__)))

@get('/site/<filename>')
def index(filename):
    return static_file(f'site/{filename}', root=os.path.dirname(os.path.abspath(__file__)))

@get('/ping')
def index():
    return 'Server running...'

@post('/chat')
def chat():
    try:
        message = request.json['message']
    except:
        raise ValueError
    
    print(f'receive: \n{message}')
    reply = chatter.chat(message)
    refine = refiner.refine(chatter.history)
    return { 'refine': refine, 'reply': reply }

if __name__ == '__main__':
    run(host='localhost', port=8080)