import os
from bottle import run, get, post, request, static_file

@get('/')
def ping():
    return 'Server running...\n'

@get('/site/<filename>')
def index(filename):
    return static_file(f'site/{filename}', root=os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)