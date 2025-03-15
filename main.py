
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/<name>")
def hello_world(name=None):
    if name is None:
        name = "idegen"
    return render_template('hello.html', person=name)


def valid_login(username, pwd):
    if username == 'admin' and pwd == 'qwe':
        return True
    return False


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['pwd']):
            return render_template('hello.html', person=request.form['username'])
        else:
            error = 'Hibás felhasználónév vagy jelszó!'

    return render_template('login.html', error=error)