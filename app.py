from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, investor! Give me your money!'


# @app.route('/login/', methods=['post', 'get'])
# def login():
#     return "Please login"

@app.route('/login/', methods=['post', 'get'])
def login():
    message = 'Please authorize or login'
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            message = "Correct username and password"
        else:
            message = "Wrong username or password"
    return render_template('login.html', message=message)
