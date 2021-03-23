from bottle import route, run, template, request
from fastapi.security import OAuth2AuthorizationCodeBearer

from ..openidclient import xxacclient


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/callback')
def index():
    #state = request.query.state
    #session_state = request.query.session_state
    code = request.query.code
    token = xxacclient.get_token("", code)
    return token

@route('/jwtcallback')
def jwt():
    state = request.query.state
    session_state = request.query.session_state
    code = request.query.code

    return code




def serve():
    run(host='localhost', port=8000)
