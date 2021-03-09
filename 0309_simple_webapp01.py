from flask import Flask, session
# 원래 HTTP는 어떤 브라우저에서 접속했는지 제대로 알지 못한다
# 이를 위해 session, 즉 세션을 사용해 어떤 브라우저에서 접속했는지를 각각 따로 설정해서 제어할 수 있다
# 예를 들어 edge에서 user명을 Alice로, 오페라에서는 John으로, 크롬에서는 Thomas라고 설정하면
# /setuser 이후 /getuser를 써도 각 브라우저 별로 지정한 이름만 남는다.
# 즉, edge에서 Alice라고 지정했다고 해서 크롬이나 오페라에서 /getuser를 해도 Alice로 지정되지 않는다.

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'        #암호

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    app.run(debug=True)
