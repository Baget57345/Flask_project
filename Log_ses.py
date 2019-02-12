from flask import Flask,session
from checker import checker_log


app = Flask(__name__)
app.secret_key ='YouWillNeverGuess'

@app.route('/')
def hello() ->str:
    return 'Hello from simple webapp.'

@app.route('/page1')
@checker_log
def page1() ->str:
    return 'This is page 1.'

@app.route('/page2')
@checker_log
def page2() ->str:
    return 'This is page 2.'

@app.route('/page2')
@checker_log
def page2() ->str:
    return 'This is page 4.'

@app.route('/page3')
@checker_log
def page3() ->str:
    return 'This is page 3.'

@app.route('/login')
def do_login() ->str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout() ->str:
    session.pop('logged_in')
    return 'Yo are now logged out'

@app.route('/status')
def check_status() ->str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are not logged in'

if __name__=='__main__':
    app.run(debug=True)