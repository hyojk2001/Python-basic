from flask import Flask, session

#로그인 상황에서도 세션은 각 브라우저를 다르게 인식한다
#즉 예를 들어서 크롬에서 로그인을 해도 오페라나 edge에서 로그인했다고 뜨지는 않는다.

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@app.route('/page1')
def page1() -> str:
    return 'this is page 1.'

@app.route('/page2')
def page2() -> str:
    return 'this is page 2.'

@app.route('/page3')
def page3() -> str:
    return 'this is page 3.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'


if __name__ == '__main__':
    app.run(debug=True)